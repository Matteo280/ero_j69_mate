import rclpy
from rclpy.node import Node
from std_msgs.msg import String
import json
import random

class IdojarasJelento(Node):
    def __init__(self):
        super().__init__('ros2_idojaras_jelento')
        self.publisher_ = self.create_publisher(String, 'weather_data', 10)
        self.timer = self.create_timer(1.0, self.publish_weather_data)

    def publish_weather_data(self):
        weather_data = {
            'homerseklet': round(random.uniform(-10, 40), 1),  # Celsius
            'paratartalom': round(random.uniform(30, 80), 1),  # Szazalek
            'szelsebesseg': round(random.uniform(0, 20), 1),   # m/s
            'idojaras_tipus': random.choice(['napsütés', 'eső', 'felhős', 'szeles'])
        }

        message = String()
        message.data = json.dumps(weather_data)

        self.publisher_.publish(message)
        self.get_logger().info(f'Küldött időjárási adatok: {message.data}')


def main(args=None):
    rclpy.init(args=args)
    node = IdojarasJelento()
    rclpy.spin(node)
    node.destroy_node()
    rclpy.shutdown()


if __name__ == '__main__':
    main()