import rclpy
from rclpy.node import Node
from std_msgs.msg import String


class RobotPublisher(Node):

    def __init__(self):
        super().__init__('robot_publisher')

        self.publisher_ = self.create_publisher(
            String,
            'robot_message',
            10
        )

        self.timer = self.create_timer(1.0, self.publish_message)

    def publish_message(self):
        msg = String()
        msg.data = 'Hi, I love Robots'

        self.publisher_.publish(msg)

        self.get_logger().info(
            'Publishing: "%s"' % msg.data
        )


def main(args=None):
    rclpy.init(args=args)

    node = RobotPublisher()
    rclpy.spin(node)

    node.destroy_node()
    rclpy.shutdown()


if __name__ == '__main__':
    main()
