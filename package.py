name = "vision_to_mavros"

version = "1.0.0"

uuid = "3df89286-1c7b-45f0-a96b-3c9047cadcca"

description = """
Forked from https://github.com/thien94/vision_to_mavros. 

This is a collection of ROS (https://www.ros.org/) and non-ROS (Python, cpp) code that converts data 
from vision-based systems (like fiducial tags, VIO, SLAM, or depth image) to corresponding 
MAVROS (http://wiki.ros.org/mavros) topics or MAVLink (https://mavlink.io/en/) messages. 

These can be consumed by a flight control stack to support precise localization and navigation tasks.
"""

authors = ["Ryan McDermid"]

requires = ["python"]

build_command = ('source /opt/ros/noetic/setup.bash && cd {root} || exit &&'
                 'catkin_make install -DCMAKE_INSTALL_PREFIX="$REZ_BUILD_INSTALL_PATH"')

variants = [
    ["platform-linux", "arch-x86_64", "os-Ubuntu-20.04"],
    ["platform-linux", "arch-aarch64", "os-Ubuntu-20.04"]
]


def post_commands():
    setup_path = expandvars("{this.root}/setup.bash")
    command(f"source {setup_path}")
