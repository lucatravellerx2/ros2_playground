ARG ROS_DISTRO="humble"
ARG START_IMAGE="ros:humble"
##
FROM $START_IMAGE

ENV SHELL /bin/bash

# Set user values
ARG USER_UID=1000
ARG USER_GID=$USER_UID
ARG NAME

# Create the user
RUN groupadd ${NAME} --gid ${USER_UID}
RUN useradd --uid $USER_UID --gid $USER_GID -m $NAME
RUN echo "${NAME}:${NAME}" | chpasswd
RUN adduser ${NAME} sudo
    # [Optional] Add sudo support. Omit if you don't need to install software after connecting.
#    && apt-get update \
#    && apt-get install -y sudo \
#    && echo $USER ALL=\(root\) NOPASSWD:ALL > /etc/sudoers.d/$USER \
#    && chmod 0440 /etc/sudoers.d/$USER
RUN apt-get update && apt-get upgrade -y
RUN apt-get install -y python3-pip iputils-ping nano openssh-client
# pi camera trying
RUN apt-get install -y libepoxy-dev libjpeg-dev 
RUN apt-get install -y libtiff5-dev libpng-dev python3 python3-dev libpython3-dev
RUN apt-get install -y g++ libevent-dev libdrm-dev libsdl2-dev
RUN apt-get install -y git python3-jinja2
RUN apt-get install -y libboost-dev libgnutls28-dev openssl pybind11-dev liblttng-ust-dev
RUN apt-get install -y cmake ninja-build
RUN apt-get install -y python3-yaml python3-ply libyaml-dev libcap-dev
RUN apt install ros-${ROS_DISTRO}-mavros -y

# install mavros libs
RUN . /opt/ros/${ROS_DISTRO}/setup.sh && ros2 run mavros install_geographiclib_datasets.sh

RUN pip install --upgrade pip

RUN pip install setuptools==58.2.0
RUN pip install numpy==1.26.4 # for pre-trained TF Lite model
RUN pip install requests

RUN apt-get install -y gdb


# create ros directory
RUN mkdir -p /ros_ws/src
#RUN #mkdir -p /tmp/src
WORKDIR /ros_ws/src
#RUN git -C px4_ros_com pull || git clone https://github.com/PX4/px4_ros_com.git
#RUN git -C px4_msgs pull || git clone https://github.com/PX4/px4_msgs.git

#ARG DISTRO
# build src nodes
COPY entryfile.sh /
RUN chmod +x /entryfile.sh

COPY build.sh /
RUN chmod +x /build.sh

RUN mkdir -p /config
RUN chown -R $NAME:$NAME /config

# Setting user and starting directory
RUN chown -R $NAME:$NAME /ros_ws
RUN adduser $NAME dialout
RUN adduser $NAME video
USER $NAME
WORKDIR /

ENTRYPOINT ["/bin/bash", "/entryfile.sh"]
CMD ["/bin/bash"]
