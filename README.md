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

Add the following code:

```python
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
```

Save and exit:

```text
Ctrl + O
Enter
Ctrl + X
```

---

## 4. Subscriber

Create the Subscriber file:

```bash
nano subscriber_LoveRobot.py
```

Add:

```python
import rclpy
from rclpy.node import Node
from std_msgs.msg import String


class RobotSubscriber(Node):

    def __init__(self):
        super().__init__('robot_subscriber')

        self.subscription = self.create_subscription(
            String,
            'robot_message',
            self.listener_callback,
            10
        )

    def listener_callback(self, msg):

        self.get_logger().info(
            'Received: "%s"' % msg.data
        )


def main(args=None):
    rclpy.init(args=args)

    node = RobotSubscriber()

    rclpy.spin(node)

    node.destroy_node()
    rclpy.shutdown()


if __name__ == '__main__':
    main()
```

Save and exit:

```text
Ctrl + O
Enter
Ctrl + X
```

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

## 2. Create the Square Controller

Open another terminal:

```bash
cd ~
nano square.py
```

Add:

```python
import rclpy
from rclpy.node import Node
from geometry_msgs.msg import Twist
import time


class Square(Node):

    def __init__(self):
        super().__init__('square_node')

        self.publisher = self.create_publisher(
            Twist,
            '/turtle1/cmd_vel',
            10
        )

        self.draw_square()

    def draw_square(self):
        msg = Twist()

        for i in range(4):

            # Move forward
            msg.linear.x = 2.0
            msg.angular.z = 0.0

            self.publisher.publish(msg)
            time.sleep(2)

            # Stop
            msg.linear.x = 0.0
            self.publisher.publish(msg)
            time.sleep(0.5)

            # Turn approximately 90 degrees
            msg.linear.x = 0.0
            msg.angular.z = 1.57

            self.publisher.publish(msg)
            time.sleep(1)

            # Stop
            msg.angular.z = 0.0
            self.publisher.publish(msg)
            time.sleep(0.5)


def main():

    rclpy.init()

    node = Square()

    node.destroy_node()
    rclpy.shutdown()


if __name__ == '__main__':
    main()
```

Save and exit:

```text
Ctrl + O
Enter
Ctrl + X
```

---

## 3. Run the Square Controller

```bash
source /opt/ros/humble/setup.bash
python3 square.py
```

The node publishes velocity commands to:

```text
/turtle1/cmd_vel
```

using the ROS 2 `Twist` message.

* `linear.x` controls forward movement.
* `angular.z` controls rotation.

The sequence is repeated four times to form the square.

---

## 📸 Task 2 Result

The screenshot below shows the final square drawn by Turtlesim.

<img width="507" height="523" alt="لقطة شاشة 2026-08-13 230005" src="https://github.com/user-attachments/assets/86fa3087-a0d3-41e4-bb3b-2d4a794b4f5e" />
<img width="506" height="537" alt="لقطة شاشة 2026-08-13 225933" src="https://github.com/user-attachments/assets/f21b7a47-85b3-4847-a68b-bfab885b236b" />
<img width="505" height="524" alt="لقطة شاشة 2026-08-13 230013" src="https://github.com/user-attachments/assets/8cf854bc-8d9c-4b25-beb5-209d8002d5ab" />

```text
📸 Turtlesim Square Result Screenshot
```

---

# 🛠️ Technologies & Concepts

* ROS 2 Humble
* Python
* `rclpy`
* Publisher / Subscriber
* ROS 2 Topics
* `std_msgs/String`
* `geometry_msgs/Twist`
* Turtlesim
* Ubuntu / WSL
* Robot motion control

---

## 🎯 What Was Applied

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

## 🎓 Training Context

These tasks were completed as part of the **ROS and AI Track during my Robotics Engineering Internship at Smart Methods**.
