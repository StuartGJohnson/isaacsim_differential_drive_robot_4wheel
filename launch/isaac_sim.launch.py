from launch import LaunchDescription
from launch_ros.actions import Node
from launch.actions import DeclareLaunchArgument
from launch.substitutions import LaunchConfiguration
import os

world_arg = DeclareLaunchArgument(
    'world',
    default_value='',
    description='Specify the world file for Issacsim'
)

# Retrieve launch configurations
world_file = LaunchConfiguration('world')
robot_file = LaunchConfiguration('robot')

def generate_launch_description():
    return LaunchDescription([
        Node(
            package='isaacsim_differential_drive_robot_4wheel',
            executable='isaac_sim_node.py',
            name='isaacsim',
            output='screen',
            parameters=[{'world': world_file, 'robot':robot_file}],
        ),
    ])