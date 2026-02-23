#!/usr/bin/env python3
import rclpy
from rclpy.node import Node
from geometry_msgs.msg import Twist

class CircleTurtleNode(Node):
    def __init__(self):
        super().__init__('circle_turtle_node')
        self.publisher_ = self.create_publisher(Twist, '/turtle1/cmd_vel', 10)
        self.timer = self.create_timer(0.1, self.move_circle)
        self.get_logger().info("Turtle mulai berjalan melingkar...")

    def move_circle(self):
        msg = Twist()
        msg.linear.x = 2.0  
        msg.angular.z = 1.0 
        self.publisher_.publish(msg)

def main(args=None):
    rclpy.init(args=args)
    node = CircleTurtleNode()
    try:
        rclpy.spin(node)
    except KeyboardInterrupt:
        pass
    node.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()