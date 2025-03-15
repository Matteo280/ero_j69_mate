from setuptools import find_packages, setup
from glob import glob
import os

package_name = 'ros2_weather_monitor'

setup(
    name=package_name,
    version='0.0.0',
    packages=find_packages(exclude=['test']),
    data_files=[
        ('share/ament_index/resource_index/packages',
            ['resource/' + package_name]),
        ('share/' + package_name, ['package.xml']),
        (os.path.join('share', package_name), glob('launch/*launch.[pxy][yma]*')), 
    ],
    install_requires=['setuptools'],
    zip_safe=True,
    maintainer='todo',
    maintainer_email='eros.mate06@gmail.com',
    description='TODO: Package description',
    license='GNU General Public License v3.0',
    tests_require=['pytest'],
    entry_points={
        'console_scripts': [
        'ros2_idojaras_jelento = ros2_weather_monitor.ros2_idojaras_jelento:main',
        'ros2_idojaras_elemzo = ros2_weather_monitor.ros2_idojaras_subscriber:main',
        ],
    },
)
