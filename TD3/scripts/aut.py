import time
from math import sin, cos, radians, atan2, degrees, sqrt
from pymavlink import mavutil

# Connect to the drone
master = mavutil.mavlink_connection('udpin:127.0.0.1:14550')
master.wait_heartbeat()

# Arm the drone
master.arducopter_arm()
print("Waiting for the vehicle to arm")
master.motors_armed_wait()
print('Armed!')

# Request GLOBAL_POSITION_INT message
master.mav.request_data_stream_send(
    master.target_system,
    master.target_component,
    mavutil.mavlink.MAV_DATA_STREAM_POSITION,
    1, 
    1 
)

# Wait for the GLOBAL_POSITION_INT message
def wait_for_message(master, message_type, timeout=5):
    start_time = time.time()
    while time.time() - start_time < timeout:
        msg = master.recv_match(type=message_type, blocking=True)
        if msg:
            return msg
    print(f"Timeout waiting for {message_type} message")
    return None

global_position_msg = wait_for_message(master, 'GLOBAL_POSITION_INT')

# Extract position data from the stored message
if global_position_msg:
    center_x = global_position_msg.lat / 1e7  
    center_y = global_position_msg.lon / 1e7 
    center_z = global_position_msg.relative_alt / 1e3 
    print(f"Current position: ({center_x}, {center_y}, {center_z})")
else:
    print("Failed to get position data")


master.mav.set_mode_send(
    master.target_system,
    mavutil.mavlink.MAV_MODE_FLAG_CUSTOM_MODE_ENABLED,
    4  # Guided mode
)

# Takeoff
master.mav.command_long_send(
    master.target_system,
    master.target_component,
    mavutil.mavlink.MAV_CMD_NAV_TAKEOFF,
    0,
    0,
    0,
    0,
    0,
    0,
    0,
    12  # Altitude in meters
)

# Wait for the drone to reach the altitude
time.sleep(15)  



# Circle Parameters
radius = 0.5  # Radius of the circle in meters
speed = 0.2  # Speed of the drone in m/s

desired_altitude = 10.0  # Altitude above home position

# Draw Circle (with yaw control and altitude correction)
yaw_angle = 0  # Initial yaw angle
for angle in range(0, 361, 2):
    x = center_x + radius * cos(radians(angle))
    y = center_y + radius * sin(radians(angle))
    z = desired_altitude 


    # Calculate desired pitch angle (simple approximation)
    pitch_angle = atan2(radius, desired_altitude)


    # master.mav.set_position_target_global_int_send(
    #     0,
    #     master.target_system,
    #     master.target_component,
    #     mavutil.mavlink.MAV_FRAME_GLOBAL_RELATIVE_ALT_INT,
    #     0b110111111000,  # Include yaw angle
    #     int(x * 1e7),
    #     int(y * 1e7),
    #     z,
    #     0, 0, 0, 0, 0, 0,
    #     radians(yaw_angle),
    #     0  
    # )

    # Calculate desired pitch angle (simple approximation)
    pitch_angle = atan2(radius, desired_altitude)

    # Calculate quaternion components
    cy = cos(yaw_angle * 0.5)
    sy = sin(yaw_angle * 0.5)
    cp = cos(pitch_angle * 0.5)
    sp = sin(pitch_angle * 0.5)

    # Construct quaternion (w, x, y, z)
    qw = cy * cp
    qx = cy * sp
    qy = sy * cp
    qz = sy * sp

    # Send command with pitch and yaw
    master.mav.set_attitude_target_send(
        0,  
        master.target_system,
        master.target_component,
        0b00000111,  # Ignore body roll rate
        [qw, qx, qy, qz],  # Q (quaternion for desired attitude)
        0, 0, 0,  # Body rates (ignored)
        0.5  # Thrust (adjust as needed)
    )
    
    yaw_angle += 2  # Increment yaw angle for each waypoint
    time.sleep(1.0)  # Increased sleep time for stability
    time.sleep(speed * 5)  # Adjust sleep time for desired speed

# Return to Launch (RTL)
master.mav.command_long_send(
    master.target_system,
    master.target_component,
    mavutil.mavlink.MAV_CMD_NAV_RETURN_TO_LAUNCH,
    0,
    0,
    0,
    0,
    0,
    0,
    0,
    0
)