#!/usr/bin/env python3

import os
import launch
import launch_ros.actions

def generate_launch_description():
    # 로봇 모델의 URDF 파일 경로
    urdf_file = os.path.join(os.getcwd(), 'urdf', 'manipulator.urdf')

    return launch.LaunchDescription([
        # control 노드 실행
        launch_ros.actions.Node(
            package='control',
            executable='control',
            name='control',
            parameters=[{'use_sim_time': True, 'robot_description': urdf_file}]
        ),
        # rviz2 런처 실행
        launch_ros.actions.Node(
            package='rviz2',
            executable='rviz2',
            name='rviz2',
            arguments=['-d', os.path.join(os.getcwd(), 'rviz', 'rviz_config.rviz')]
        )
    ])

