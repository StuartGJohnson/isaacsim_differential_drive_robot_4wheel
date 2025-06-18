# 4-Wheel Differential Drive Robot Simulation (IsaacSim)

## About

This package provides a (custom) 4-wheel skid-steer robot for simulation in isaacsim. 
It also provides scripts for launching the robot. World generation is not included
in this package.

## Requirements

This package was developed on Ubuntu 22.04/ROS2 Humble/IsaacSim 4.5.

#### Install Required ROS 2 Packages

Many ROS2 packages are required. Keep installing until it works.

## Usage

### Clone the Repository

### Build the Package

Source the ROS 2 environment and build the package. In your ros2 ws directory:


```bash
source /opt/ros/humble/setup.bash #(if necessary)
colcon build
colcon source install/setup.bash
```

### Launch the Robot

After building the package, and given a world file with accompanying launch metadata:

```bash
ros2 launch isaacsim_differential_drive_robot_4wheel isaac_sim.launch.py world:=<world>.usda
```

This script assumes an accompanying "\<world\>.yml" file such as:

```yml
area:
- 40.0
- 20.0
resolution: 2.0
robot_start_xy:
- -2.0
- 0.0
robot_stop_xy:
- 10.0
- -8.0
scale: 0.4
seed: 41
threshold: 0.0
```

The important data here is robot_start_xy.

### Control the Robot

#### Using a Keyboard

You can control the robot using the ```teleop_twist_keyboard``` package:

```bash
ros2 run teleop_twist_keyboard teleop_twist_keyboard
```
## Sensor Support

## Transform Tree

## Open-loop robot behavior

## Controller issues

There are issues in IsaacSim with skid-steer robots with multiple axles. In Gazebo,
the essential settings to make skid-steer robots work well (or at least simply) was
the addition of tire slip. See the section on Open-loop behavior. In addition, see:

<a href="https://forums.developer.nvidia.com/t/how-to-drive-clearpath-jackal-via-ros2-messages-in-isaac-sim/275907"> Discussion of skid-steer issues 1</a>
<a href="https://forums.developer.nvidia.com/t/wheel-robot-with-4-joints-cant-move-by-differential-controller-using-action-graph-and-ros/228800/9"> Discussion of skid-steer issues 2</a>