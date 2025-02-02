# Development of an Autonomous Drone Navigation System in a Simulated Environment Using ROS 2 Humble Hawksbill, Gazebo Harmonic, and ArduPilot

## Objective
To develop a simulated environment using ROS 2 Humble Hawksbill, Gazebo Harmonic, and ArduPilot to facilitate autonomous drone navigation. This environment will enable the testing and validation of autonomous navigation algorithms, focusing on obstacle avoidance and efficient path planning within complex scenarios. The simulation will integrate real-time sensor data, drone control, and environmental interactions, providing a robust platform for the development and refinement of navigation strategies before hardware implementation.
## Project Overview

For a detailed overview of the project, including background information, methodology, and repository structure, please refer to the [Project Overview](docs/project_overview.md) document.

## Project Structure
```
ros2_humble_gz-sim/               # Root directory of your ROS 2 Humble Gazebo simulation project.
├── ros2_gz_pkg/                  # Main ROS 2 package directory.
│   ├── config/                   # Configuration files (e.g., YAML) for parameters and settings.
│   ├── launch/                   # Launch files (.launch.py) to start nodes and simulations.
│   ├── models/                   # Custom 3D models for Gazebo simulations.
│   ├── py_launch_example/        # Example directory for Python-based launch scripts.
│   ├── resource/                 # Additional resources like URDF files and materials.
│   ├── rviz/                     # RViz configuration files (.rviz) for visualization.
│   ├── scripts/                  # Custom Python scripts for nodes and utilities.
│   ├── test/                     # Test files for unit and integration testing.
│   ├── worlds/                   # Gazebo world files (.sdf or .world) defining the simulation environment.
│   ├── LICENCE/                  # License file for the project.
│   ├── package.xml/              # ROS 2 package manifest with dependencies and metadata.
│   ├── setup.cfg/                # Python packaging configuration file.
│   ├── setup.py/                 # Python setup script for package installation.
├── README.md                     # Project overview and documentation.

```


## Setup Instructions

### Prerequisites

#### 1. Operating System
- Ubuntu 22.04 : The project is designed to run on Ubuntu 22.04, ensuring compatibility with ROS 2 Humble.

#### 2. Development Tools
- Git
- Python 3.8+
- pip (Python package installer)

#### 3. Robotics Middleware
- ROS 2 Humble Hawksbill: The ROS distribution used for robot control and communication.

#### 4. Simulation Environment
- Gazebo Harmonic : Simulation environment compatible with ROS 2

#### 5. Drone Firmware and Control
- ArduPilot : Open-source autopilot firmware for controlling the drone in simulation.

#### 6. Flight Controller
- Cube Orange

#### 7. Companion Computer
- Raspberry Pi 5

#### 8. Communication Interface
- MAVROS

#### 9. Ground Control Software
- QGroundControl (QGC)

#### 10. Python Libraries
- NumPy
- Stable Baselines3
- Gym
- Matplotlib (for plotting and visualization)
- pandas (for data analysis)
- Jupyter Notebook (for interactive development)

#### 11. Additional Tools
- Colcon (ROS2 build tool)
- Wget (for downloading dependencies)
- curl (for downloading dependencies)

### Installation Steps

1. **Install ROS2 Humble Hawksbill**

- Follow the steps in [ROS 2 Installation](https://docs.ros.org/en/humble/Installation/Ubuntu-Install-Debians.html)

2. **Install Gazebo Harmonic**
- Follow the steps in [Gazebo Harmonic Installation](https://gazebosim.org/docs/latest/install_ubuntu/)

<!-- 3. **Install MAVROS** -->


3. **Clone and Set Up ArduPilot with Gazebo for Simulation**

- Follow this git repo to install Ardupilot[Ardupilot](https://github.com/ArduPilot/ardupilot/tree/master)

4. **Set Up the Environment for Gazebo Models and Plugins**

- Follow this git repo to install Ardupilot[Ardupilot Gazebo](https://github.com/ArduPilot/ardupilot_gazebo)

5. **Install Python Libraries**

6. **Install QGroundControl**

Before installing QGroundControl for the first time:
- 1. On the command prompt enter
```bash
sudo usermod -a -G dialout $USER
sudo apt-get remove modemmanager -y
sudo apt install gstreamer1.0-plugins-bad gstreamer1.0-libav gstreamer1.0-gl -y
sudo apt install libfuse2 -y
sudo apt install libxcb-xinerama0 libxkbcommon-x11-0 libxcb-cursor-dev -y
```
- 2. Logout and login again to enable the change to user permissions.
  - To install QGroundControl:

- 3. Download QGroundControl.AppImage.
   - Install (and run) using the terminal commands:
```bash
chmod +x ./QGroundControl.AppImage
./QGroundControl.AppImage  (or double click)
```

## Running the Simulation

1. **Launch the Gazebo Environment and RViz**
    ```bash
    ros2 launch py_launch_example iris_maze.launch.py
    ```

2. **Start the ArduPilot Simulation**
    ```bash
    sim_vehicle.py -v ArduCopter -f gazebo-iris --console --map 
    ```



## Contributing

Please see the  [CONTRIBUTING.md](/docs/contributing.md) file for guidelines on how to contribute to this project.


## License
This project is licensed under the [MIT License](/LICENSE).

## Contact
For any questions or issues, please open an issue on the GitHub repository or contact the project maintainer.
