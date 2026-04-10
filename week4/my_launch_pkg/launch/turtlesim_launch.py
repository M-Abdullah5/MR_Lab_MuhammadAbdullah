from launch import LaunchDescription
from launch_ros.actions import Node

def generate_launch_description():
    return LaunchDescription([
        # Start the simulation window
        Node(
            package='turtlesim',
            executable='turtlesim_node',
            name='sim'
        ),
        # Start our custom Follower node
        Node(
            package='my_launch_pkg',
            executable='follower_node',
            name='follower'
        )
    ])
