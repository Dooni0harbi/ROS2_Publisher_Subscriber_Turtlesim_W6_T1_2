import rclpy
from rclpy.node import Node
from geometry_msgs.msg import Twist
import time


class Square(Node):

    def __init__(self):
        super().__init__('square_node')

        self.publisher = self.create_publisher(
            Twist,
            '/turtle1/cmd_vel',
            10
        )

        self.draw_square()

    def draw_square(self):
        msg = Twist()

        for i in range(4):

            # Move forward
            msg.linear.x = 2.0
            msg.angular.z = 0.0
            self.publisher.publish(msg)
            time.sleep(2)

            # Stop
            msg.linear.x = 0.0
            self.publisher.publish(msg)
            time.sleep(0.5)

            # Turn approximately 90 degrees
            msg.linear.x = 0.0
            msg.angular.z = 1.57
            self.publisher.publish(msg)
            time.sleep(1)

            # Stop
            msg.angular.z = 0.0
            self.publisher.publish(msg)
            time.sleep(0.5)


def main():
    rclpy.init()

    node = Square()

    node.destroy_node()
    rclpy.shutdown()


if __name__ == '__main__':
    main()
