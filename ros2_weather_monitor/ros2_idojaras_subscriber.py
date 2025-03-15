import rclpy
from rclpy.node import Node
from std_msgs.msg import String
import json
import random

class IdojarasElemzo(Node):
    def __init__(self):
        super().__init__('ros2_idojaras_elemzo')
        self.subscription = self.create_subscription(
            String,
            'weather_data',
            self.listener_callback,
            10)
        self.subscription  # prevent unused variable warning

    def listener_callback(self, msg):
        data = json.loads(msg.data)
        self.get_logger().info(f'Megkapott időjárási adatok: {data}')


def main(args=None):
    rclpy.init(args=args)
    node = IdojarasElemzo()
    rclpy.spin(node)
    node.destroy_node()
    rclpy.shutdown()


if __name__ == '__main__':
    main()