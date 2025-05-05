#!/bin/bash
#set -e

source /opt/ros/$ROS_DISTRO/setup.bash
#rm -rf /ros_ws/build
#rm -rf /ros_ws/install
cd /ros_ws/ && colcon build --symlink-install
