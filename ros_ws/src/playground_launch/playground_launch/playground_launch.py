from launch import LaunchDescription
from launch_ros.actions import Node
from launch.actions import RegisterEventHandler
from launch.event_handlers import OnProcessStart

# from dotenv import load_dotenv
import os

def generate_launch_description():

    # load_dotenv()

    pub_version = int(os.getenv("PUBLISHER_RUN"))

    launch_description = LaunchDescription()

    whitelist_pub_node = Node(
            package='python_playground',
            executable='interface_whitelist_pub',
            name='interface_whitelist_pub'
        )
    
    whitelist_sub_node = Node(
            package='python_playground',
            executable='interface_whitelist_sub',
            name='interface_whitelist_sub'
        )
    
    bacon_one_pub_node = Node(
            package='python_playground',
            executable='b1pub',
            name='b1pub'
        )
    
    bacon_one_sub_node = Node(
            package='python_playground',
            executable='b1sub',
            name='b1sub'
        )
    
    bacon_two_pub_node = Node(
            package='python_playground',
            executable='b2pub',
            name='b2pub'
        )
    
    bacon_two_sub_node = Node(
            package='python_playground',
            executable='b2sub',
            name='b2sub'
        )
    
    if pub_version == 1:
        first_node = RegisterEventHandler(
            event_handler=OnProcessStart(
                target_action=whitelist_pub_node,
                on_start=[
                    bacon_one_pub_node
                ]
            )
        )
    
        second_node = RegisterEventHandler(
                event_handler=OnProcessStart(
                    target_action=bacon_one_pub_node,
                    on_start=[
                    bacon_two_pub_node
                    ]
                )
            )
        
        launch_description.add_action(whitelist_pub_node)
        launch_description.add_action(first_node)
        launch_description.add_action(second_node)
    else:
        first_node = RegisterEventHandler(
            event_handler=OnProcessStart(
                target_action=whitelist_sub_node,
                on_start=[
                    bacon_one_sub_node
                ]
            )
        )
    
        second_node = RegisterEventHandler(
                event_handler=OnProcessStart(
                    target_action=bacon_one_sub_node,
                    on_start=[
                    bacon_two_sub_node
                    ]
                )
            )
        launch_description.add_action(whitelist_sub_node)
        launch_description.add_action(first_node)
        launch_description.add_action(second_node)

    
    return launch_description
