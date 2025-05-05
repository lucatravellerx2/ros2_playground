#!/bin/bash

# source environment files
source /opt/ros/$ROS_DISTRO/setup.bash
source /ros_ws/install/setup.bash


ros2 launch playground_launch python_playground_launch.py