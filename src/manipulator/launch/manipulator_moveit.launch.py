import os

from ament_index_python.packages import get_package_share_directory
from launch import LaunchDescription
from launch_ros.actions import Node


def generate_launch_description():
    # URDF 파일 경로 설정
    pkg_share = get_package_share_directory('manipulator')
    urdf_file = os.path.join(pkg_share, 'urdf', 'manipulator.urdf')
    srdf_file = os.path.join(pkg_share, 'config', 'manipulator.srdf')

    # move_group 노드 실행
    return LaunchDescription([
        Node(
            package='moveit_ros_move_group',
            executable='move_group',
            name='move_group',
            output='screen',
            parameters=[{
                'robot_description': open(urdf_file).read(),
                'robot_description_semantic': open(srdf_file).read(),
                'move_group': 'manipulator',
                'joint_names': ['motor1', 'motor2', 'motor3',
                                'motor4', 'motor5', 'motor6']
            }]
        )
    ])
