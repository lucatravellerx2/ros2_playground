from launch import LaunchDescription
from launch_ros.actions import Node

def generate_launch_description():
    return LaunchDescription([
        Node(
            package='python_playground',
            namespace='python_playground',
            executable='inter_pub',
            name='inter_pub'
        ),
    ])
