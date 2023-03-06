#!/usr/bin/env python3

import rclpy
from rclpy.node import Node
from trajectory_msgs.msg import JointTrajectory, JointTrajectoryPoint


class Control(Node):

    def __init__(self):
        super().__init__('control')
        self.publisher_ = self.create_publisher(JointTrajectory, 'joint_trajectory', 10)

        timer_period = 0.1  # seconds
        self.timer = self.create_timer(timer_period, self.timer_callback)
        self.i = 0
        self.joint_names = ['motor1', 'motor2', 'motor3', 'motor4', 'motor5', 'motor6']
        self.joint_positions = [0.0, 0.0, 0.0, 0.0, 0.0, 0.0]

    def timer_callback(self): # Create JointTrajectory msg, Append to messages with updates from each location
        self.i += 1
        msg = JointTrajectory()
        msg.joint_names = self.joint_names
        point = JointTrajectoryPoint() # joint control
        point.positions = self.joint_positions
        point.time_from_start = self.get_clock().now().to_msg()
        msg.points.append(point)
        self.publisher_.publish(msg)
        self.get_logger().info('Publishing trajectory %d' % self.i)
        if self.i == 50:
            self.get_logger().info('Shutting down node...')
            self.timer.cancel()
            self.destroy_node()
            rclpy.shutdown()

def main(args=None):
    rclpy.init(args=args)

    control_node = Control()

    rclpy.spin(control_node)

    control_node.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()

