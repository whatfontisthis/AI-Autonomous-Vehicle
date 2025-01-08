# **Museum Curator Robot Project**

## **Overview**

This project was developed to enhance museum visitor experiences by providing seamless guidance and exhibit information using an **AI-powered autonomous curator robot**. Inspired by existing systems like **museum curator bots** and **Incheon Airport's "AIRSTAR" robot**, this project offers a cost-effective and efficient solution to improve museum exploration.

---

## **Project Objectives**

1. Enable **real-time map updates** when the museum layout changes.
2. Use **AI and deep learning** to improve exhibit recognition accuracy via camera.
3. Provide **navigation services** to guide visitors to their desired exhibits.
4. Develop an easy-to-use **GUI** for administrators and visitors.

---

## **Features**

### **Core Functionalities**
1. **Admin GUI Features**:
   - Real-time camera feed from the robot to the admin PC.
   - Manual and automatic mapping options for layout updates.
   - Exhibit inventory display for the museum.
   - Easy selection of exhibits for visitor guidance.

2. **Navigation Improvements**:
   - Optimal pathfinding to destinations.
   - Precise movement to target locations with minimal errors.
   - Automatic map generation and saving.

3. **Advanced Algorithms**:
   - Wall-following navigation for mapping.
   - Dynamic obstacle avoidance using **D\*** algorithm.

4. **Visitor and Exhibit Management**:
   - Add or remove exhibits dynamically through a user-friendly interface.
   - Display exhibit recognition data on the admin screen.

---

## **Tech Stack**

- **AI & Machine Learning**: TensorFlow, MediaPipe, OpenCV
- **Robotics**: ROS (Robot Operating System) - ROS1 Melodic
- **Operating System**: Linux Ubuntu 18.04
- **Programming Language**: Python 3.6.9
- **UI Framework**: PyQt5

---

## **Key Technologies**

### **Robotics**
- **SLAM & Navigation**:
  - Map generation and navigation using **ROS SLAM**.
  - Algorithms for real-time position estimation and navigation.
  
- **Dynamic Obstacle Avoidance**:
  - Path optimization with obstacle detection.

### **Deep Learning**
- **Object Detection**:
  - Use AI to recognize and classify exhibits for accurate guidance.

### **GUI for User Interaction**
- **Admin Controls**:
  - Monitor and update robot operations.
  - Manage exhibits and navigation preferences.

---

## **Example Demonstrations**

- **TurtleBot3 Simulation**:
  ![Simulation](https://github.com/whatfontisthis/AI-Autonomous-Vehicle/raw/main/imgs/simul.gif)

- **SLAM Implementation**:
  ![SLAM](https://github.com/whatfontisthis/AI-Autonomous-Vehicle/raw/main/imgs/SLAM.gif)

- **Wall-Following Algorithm**:
  ![Wall Follower](https://github.com/whatfontisthis/AI-Autonomous-Vehicle/raw/main/imgs/wallFollow.gif)

- **Move to Destination**:
  ![Move](https://github.com/whatfontisthis/AI-Autonomous-Vehicle/raw/main/imgs/godestination.gif)

- **GUI Implementation**:
  ![GUI 1](https://github.com/whatfontisthis/AI-Autonomous-Vehicle/raw/main/imgs/gui1.gif)
  ![GUI 2](https://github.com/whatfontisthis/AI-Autonomous-Vehicle/raw/main/imgs/gui2.gif)

---

## **Project Management**

1. **Git/GitHub**:  
   - Repository for code management and collaboration.  

2. **Notion**:  
   - [Task Management]
   - [Issue Tracking](https://github.com/whatfontisthis/AI-Autonomous-Vehicle/raw/main/imgs/issues.png)

3. **Slack**:  
   - Daily development logs and discussions.  
   - File sharing and collaboration.

---

## **Challenges and Future Improvements**

### **1. Navigation Pose Estimation**
- **Current Status**: 2D maps are saved and loaded but calibration errors occur, leading to accumulated location inaccuracies.  
- **Improvement Plan**:  
  - Use SLAM calibration methods for navigation.  
  - Refine depth-based pose estimation algorithms.

### **2. Full Autonomous Drive**
- **Current Status**: Full automation not yet achieved due to integration errors during GUI and navigation synchronization.  
- **Improvement Plan**:  
  - Introduce quadrant-based navigation logic.  
  - Implement map closure and scan completeness checks.

### **3. Object Recognition Accuracy**
- **Current Status**: Limited by insufficient labeled training data.  
- **Improvement Plan**:  
  - Utilize auto-labeling tools for faster data preparation.  
  - Allocate more time for dataset collection and preprocessing.

---

## **References**

### **Core Repositories Used**
- [Stella N2](https://github.com/ntrexlab/STELLA_REMOTE_PC_N2)  
- [TurtleBot3 Simulations](https://github.com/ROBOTIS-GIT/turtlebot3_simulations)  
- [Cartographer (SLAM)](https://github.com/cartographer-project/cartographer)  
- [TensorFlow Examples](https://github.com/tensorflow/examples)  

### **Additional Resources**
- [Cartographer ROS](https://github.com/cartographer-project/cartographer_ros)  
- [SLAM GMapping](https://github.com/ros-perception/slam_gmapping)  
- [TensorFlow Object Detection](https://github.com/EdjeElectronics/TensorFlow-Object-Detection-on-the-Raspberry-Pi)  
- [Wall Follower Example](https://github.com/nimbekarnd/Wall-follower-in-ROS-using-Python)  