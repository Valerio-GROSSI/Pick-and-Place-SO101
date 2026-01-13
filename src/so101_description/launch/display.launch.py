import os
from launch import LaunchDescription
from launch_ros.actions import Node
from ament_index_python.packages import get_package_share_directory

def generate_launch_description():
    urdf_path = os.path.join(
        get_package_share_directory("so101_description"),
        "urdf",
        "so101.xacro"
    )

    return LaunchDescription([

        Node(
            package="robot_state_publisher",
            executable="robot_state_publisher",
            parameters=[{"robot_description": open(urdf_path).read()}]
        ),

        Node(
            package="joint_state_publisher",
            executable="joint_state_publisher"
        ),

        Node(
            package="rviz2",
            executable="rviz2"
        )
    ])

