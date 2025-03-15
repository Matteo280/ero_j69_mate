🌦️ ROS2 Időjárás Figyelő Rendszer

Ez a projekt egy egyszerű ROS2 alapú időjárás figyelő rendszer, amely két node-ból áll: egy adatokat küldő és egy adatokat fogadó node-ból.

📂 Projekt Struktúra

Node-ok:

🚀 ros2_idojaras_jelento - Időjárási adatokat generáló és közzétevő node.

📡 ros2_idojaras_elemzo - Az időjárási adatokat fogadó és naplózó node.

✅ Előfeltételek

🛠️ ROS2 (Foxy, Galactic vagy Humble)

🐍 Python 3.x

ROS2 csomagok: rclpy, std_msgs, launch, launch_ros

🛠️ Telepítés

1️⃣ ROS2 munkaterület létrehozása:

mkdir -p ~/ros2_weather_monitor_ws/src
cd ~/ros2_weather_monitor_ws/src

2️⃣ Projekt klónozása:

git clone <a-te-repozitoriumod-url-ja> ros2_weather_monitor

3️⃣ Függőségek telepítése és build:

cd ~/ros2_weather_monitor_ws
rosdep install --from-paths src --ignore-src -r -y
colcon build

4️⃣ Munkaterület forrásolása:

source ~/ros2_weather_monitor_ws/install/setup.bash

🚀 Futtatás

Indítsd el a launch fájlt, amely mindkét node-ot elindítja:

ros2 launch ros2_weather_monitor idojaras_launch.py

📄 Fájlok Leírása

🟢 ros2_idojaras_jelento.py: Időjárási adatokat generál és publikál a weather_data témán.

🟡 ros2_idojaras_elemzo.py: Feliratkozik a weather_data témára és naplózza az adatokat.

🔥 idojaras_launch.py: A két node együttes indítását végzi.

🔧 Fejlesztési Lehetőségek

Valós időjárási API integrálása.

További adatelemzési lehetőségek beépítése.

📚 További Információk

📖 ROS2 hivatalos dokumentáció

