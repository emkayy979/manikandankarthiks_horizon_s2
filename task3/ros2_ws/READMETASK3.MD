ROS2 Distance Sensor – Publisher & Subscriber
One node sends out random distance values, another node receives and prints them.

What This Does

Publisher node – generates a random  value every second and sends it on topic called   /rover_distance
Subscriber node –  it listens to that topic and prints every value that it gets.

Requirements

Ubuntu 22.04
ROS2 Humble


SET UP!!

1. Clone or copy the package into your workspace
~/ros2_ws/src/distance_sensor/

2. Build the package

cd ~/ros2_ws
colcon build
3. Source the workspace
source ~/ros2_ws/install/setup.bash




RUNNING:

You need two terminals open at the same time, one for each node.
terminal 1: 
  source ~/ros2_ws/install/setup.bash
ros2 run distance_sensor publisher

terminal 2: 
  source ~/ros2_ws/install/setup.bash
ros2 run distance_sensor subscriber
