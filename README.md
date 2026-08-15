# 🤖 ROS 2 Publisher & Subscriber + Turtlesim Square

This project demonstrates two practical **ROS 2 tasks using Python**:

1. Creating a **Publisher and Subscriber** to exchange a custom message.
2. Controlling **Turtlesim** to automatically draw a square.

All commands and Python code are documented directly in this README.

---

# 📡 Task 1 — Publisher & Subscriber

## Objective

Create a ROS 2 **Publisher** and **Subscriber**.

The Publisher continuously sends:

```text
Hi, I love Robots
```

The Subscriber receives and displays the same message.

The communication follows:

```text
Publisher → Topic → Subscriber
```

---

## 1. Create the ROS 2 Workspace

```bash
mkdir -p ~/ros2_ws/src
cd ~/ros2_ws/src
```

---

## 2. Create the ROS 2 Package

```bash
ros2 pkg create --build-type ament_python my_robot_pkg --dependencies rclpy std_msgs
```

Move to the Python package directory:

```bash
cd ~/ros2_ws/src/my_robot_pkg/my_robot_pkg
```

---

## 3. Publisher

Create the Publisher file:

```bash
nano publisher_LoveRobot.py
```

Open the project file:

publisher_LoveRobot.py

Copy its code and paste it into the file created in the terminal.

Save the file:

Ctrl + O
Enter
Ctrl + X

---
## 4. Subscriber

Create the Subscriber file:

```bash
nano subscriber_LoveRobot.py
```

Open the project file:

subscriber_LoveRobot.py

Copy its code and paste it into the file created in the terminal.

Save and exit:

Ctrl + O
Enter
Ctrl + X

---

## 5. Run the Publisher

Open the first terminal:

```bash
cd ~/ros2_ws
source /opt/ros/humble/setup.bash
```

Run:

```bash
python3 src/my_robot_pkg/my_robot_pkg/publisher_LoveRobot.py
```

The Publisher sends:

```text
Publishing: "Hi, I love Robots"
```

---

## 6. Run the Subscriber

Open another terminal:

```bash
cd ~/ros2_ws
source /opt/ros/humble/setup.bash
```

Run:

```bash
python3 src/my_robot_pkg/my_robot_pkg/subscriber_LoveRobot.py
```

The Subscriber receives:

```text
Received: "Hi, I love Robots"
```

---

## 📸 Task 1 Result

The screenshot below shows the Publisher and Subscriber running simultaneously and exchanging the custom ROS 2 message.

<img width="1448" height="314" alt="لقطة شاشة 2026-08-13 224850" src="https://github.com/user-attachments/assets/3cff4d32-b11e-44fb-b82a-c1b5503c183f" />

```text
📸 Publisher & Subscriber Result Screenshot
```

---

# 🐢 Task 2 — Drawing a Square with Turtlesim

## Objective

Use ROS 2 and Python to control the Turtlesim robot and automatically draw a **square**.

The movement sequence is:

```text
Move Forward
     ↓
Turn 90°
     ↓
Move Forward
     ↓
Turn 90°
     ↓
Repeat ×4
```

---

## 1. Start Turtlesim

Open a terminal:

```bash
source /opt/ros/humble/setup.bash
ros2 run turtlesim turtlesim_node
```

Keep the Turtlesim window running.

---

## 2. Open Another Terminal

Open a second terminal and enter Ubuntu/WSL if needed:

```bash
wsl
```

Then return to the Home directory:

```bash
cd ~
```

---

## 3. Create the Square Controller File

Create the Python file:

```bash
nano square.py
```

Open the project file:

`square.py`

Copy its code and paste it into the file created in the terminal.

Save the file:

**Ctrl + O** → **Enter**

Then exit:

**Ctrl + X**

---

## 4. Run the Square Controller

Source ROS 2:

```bash
source /opt/ros/humble/setup.bash
```

Then run the Python controller:

```bash
python3 square.py
```

The node sends velocity commands to the following ROS 2 topic:

```text
/turtle1/cmd_vel
```

using the ROS 2 `Twist` message.

The turtle moves forward and rotates approximately **90°** four times to form a square.

---

## 📸 Task 2 Result

The screenshot below shows the final square drawn by Turtlesim.

<img width="506" height="537" alt="لقطة شاشة 2026-08-13 225933" src="https://github.com/user-attachments/assets/f21b7a47-85b3-4847-a68b-bfab885b236b" />
<img width="507" height="523" alt="لقطة شاشة 2026-08-13 230005" src="https://github.com/user-attachments/assets/86fa3087-a0d3-41e4-bb3b-2d4a794b4f5e" />
<img width="505" height="524" alt="لقطة شاشة 2026-08-13 230013" src="https://github.com/user-attachments/assets/8cf854bc-8d9c-4b25-beb5-209d8002d5ab" />

```text
📸 Turtlesim Square Result Screenshot
```

---
## 📂 Project Structure

```text
ROS2_Publisher_Subscriber_Turtlesim_W6_T1_2/
│
├── README.md
├── publisher_LoveRobot.py
├── subscriber_LoveRobot.py
└── square.py
```

## 🛠️ Technologies Used

ROS 2 Humble
Python
rclpy
Publisher / Subscriber
ROS 2 Topics
std_msgs
geometry_msgs
Turtlesim
Ubuntu / WSL
---

## 🎯 Concepts Applied

### Publisher / Subscriber Communication

The first task demonstrates ROS 2 node communication:

```text
Publisher
    ↓
robot_message Topic
    ↓
Subscriber
```

The Publisher sends the custom message:

```text
Hi, I love Robots
```

and the Subscriber listens to the same topic and receives it.

### Turtlesim Motion Control

The second task demonstrates basic robot motion control by publishing `Twist` velocity commands to:

```text
/turtle1/cmd_vel
```

Linear and angular velocities are combined to create four straight movements and four approximately 90° rotations, forming a square.

---

##  Training Context

These tasks were completed as part of the **ROS and AI Track during my Robotics Engineering Internship at Smart Methods**.
