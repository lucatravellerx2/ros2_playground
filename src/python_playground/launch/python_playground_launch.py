from launch import LaunchDescription
from launch_ros.actions import Node

def generate_launch_description():
    return LaunchDescription([
        Node(
            package='python_playground',
            namespace='python_playground',
            executable='service_node',
            name='service_node'
        ),
        Node(
            package='python_playground',
            namespace='python_playground',
            executable='tester_node',
            name='tester_node'
        ),

        Node(
           package="python_playground",
           namespace="python_playground",
           executable="logger_node",
           name="logger_node" 
        )
    ])
