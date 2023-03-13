import os

from ament_index_python.packages import get_package_share_directory
from launch import LaunchDescription
from launch_ros.actions import Node


def generate_launch_description():
    # URDF 파일 경로 설정
    pkg_share = get_package_share_directory('manipulator')
    urdf_file = os.path.join(pkg_share, 'urdf', 'manipulator.urdf')

    return LaunchDescription([
        # robot_state_publisher 실행
        Node(
            package='robot_state_publisher',
            executable='robot_state_publisher',
            name='robot_state_publisher',
            output='screen',
            parameters=[{'robot_description': open(urdf_file).read()}]
        )
    ])
