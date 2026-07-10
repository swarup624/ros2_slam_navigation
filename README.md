# 🤖 ROS2 SLAM & Navigation

A ROS 2 Jazzy project demonstrating autonomous mobile robot navigation using SLAM, Nav2, Gazebo Harmonic, and RViz2.

---

## 📌 Features

- ✅ ROS 2 Jazzy
- ✅ Gazebo Harmonic Simulation
- ✅ Robot State Publisher
- ✅ URDF/Xacro Robot Model
- ✅ LiDAR Integration
- ✅ SLAM Mapping
- ✅ Map Saving
- ✅ AMCL Localization
- ✅ Nav2 Navigation
- ✅ Waypoint Navigation
- ✅ RViz2 Visualization

---

## 🛠 Technologies

- ROS 2 Jazzy
- Gazebo Harmonic
- RViz2
- Nav2
- SLAM Toolbox
- URDF
- Xacro
- Python
- ros_gz_bridge

---

## 📂 Project Structure

```
ros2_ws_lv3
│
├── src
│   ├── my_robot_description
│   ├── my_robot_navigation
│   ├── my_robot_bringup
│   └── ...
│
├── README.md
└── .gitignore
```

---

## 🚀 Build

```bash
cd ~/ros2_ws_lv3

colcon build --symlink-install

source install/setup.bash
```

---

## ▶️ Launch Simulation

```bash
ros2 launch my_robot_bringup bringup.launch.py
```

---

## 🗺️ Create Map

```bash
ros2 launch slam_toolbox online_async_launch.py use_sim_time:=true
```

Save the map:

```bash
ros2 run nav2_map_server map_saver_cli -f maps/my_map
```

---

## 🚗 Navigation

```bash
ros2 launch my_robot_bringup navigation.launch.py
```

---

## 📷 Screenshots

### Gazebo

(Add screenshot here)

### RViz

(Add screenshot here)

### Generated Map

(Add screenshot here)

---

## 📈 Future Improvements

- Obstacle avoidance
- Dynamic path planning
- Multi-goal navigation
- Camera-based navigation
- Autonomous exploration

---

## 👨‍💻 Author

**Swarup Jadhav**

B.Tech Automation & Robotics

GitHub: https://github.com/swarup624
