ROS2 Időjárás Figyelő Rendszer

Ez a projekt két ROS2 node-ot tartalmaz, amelyek időjárási adatokat szimulálnak és fogadnak. Az egyik node véletlenszerű időjárási adatokat generál és közzéteszi őket, míg a másik node feliratkozik ezekre az adatokra és feldolgozza őket.

Projekt Áttekintés

Node-ok:

ros2_idojaras_jelento - Egy kiadó node, amely szimulálja az időjárási adatokat.

ros2_idojaras_elemzo - Egy feliratkozó node, amely fogadja és naplózza az időjárási adatokat.

Funkcionalitás:

ros2_idojaras_jelento: Periódikusan közzéteszi a szimulált időjárási adatokat, például hőmérsékletet, páratartalmat, szélsebességet és az időjárás típusát.

ros2_idojaras_elemzo: Várja az időjárási adatokat, majd naplózza a megkapott információkat.

Előfeltételek

ROS2 (pl. ROS2 Foxy, Galactic vagy Humble)

Python 3.x

A következő ROS2 csomagok:

rclpy

std_msgs

launch

launch_ros

Telepítés és Beállítás

ROS2 Telepítése: Ha még nincs telepítve, kövesd a ROS2 telepítési útmutatót.

Létrehozunk egy ROS2 munkaterületet:

mkdir -p ~/ros2_weather_monitor_ws/src
cd ~/ros2_weather_monitor_ws/src

Klónozd a projektet:

Ha a projekt fájljaid egy Git repozitóriumban vannak, klónozd a repót a ROS2 munkaterület src mappájába:

git clone <a-te-repozitoriumod-url-ja> ros2_weather_monitor

Telepítsd a függőségeket:

A munkaterületen belül telepítsd a szükséges csomagokat és építsd fel a munkaterületet:

cd ~/ros2_weather_monitor_ws
rosdep install --from-paths src --ignore-src -r -y
colcon build

Forrásold a munkaterületet:

source ~/ros2_weather_monitor_ws/install/setup.bash

A Rendszer Futtatása

A node-ok indítása: A rendszert a launch fájl segítségével indíthatod el.

ros2 launch ros2_weather_monitor idojaras_launch.py

Ezzel mindkét node elindul: a ros2_idojaras_jelento (időjárási adatokat küldő node) és a ros2_idojaras_elemzo (adatokat fogadó és naplózó node).

Fájlok Magyarázata

ros2_idojaras_jelento.py: Kiadó node, amely véletlenszerű időjárási adatokat generál és közzéteszi őket a weather_data témán.

ros2_idojaras_elemzo.py: Feliratkozó node, amely fogadja az időjárási adatokat és naplózza azokat.

idojaras_launch.py: A launch fájl, amely egyszerre indítja el mindkét node-ot.

Fejlesztési és Bővítési Lehetőségek

Az időjárási adatok szimulációjának pontosabbá tétele, pl. valós adatforrások használatával.

További elemzési lehetőségek hozzáadása, például a szélsebesség és hőmérséklet hatásainak vizsgálata.

További Információk

További segítséget és információkat a ROS2 dokumentációban találhatsz.
