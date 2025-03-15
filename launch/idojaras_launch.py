from launch import LaunchDescription
from launch_ros.actions import Node

def generate_launch_description():
    return LaunchDescription([
        Node(
            package='ros2_weather_monitor',
            executable='ros2_idojaras_jelento',
            name='idojaras_jelento'
        ),
        Node(
            package='ros2_weather_monitor',
            executable='ros2_idojaras_elemzo',
            name='idojaras_elemzo'
        )
    ])