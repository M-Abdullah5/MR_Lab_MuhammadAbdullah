# Deliverable 5: Observations on Motion Discrepancies

During the teleoperation of the TurtleBot3 within the Gazebo environment, several discrepancies were observed between the expected (ideal kinematic) motion and the actual simulated motion:

* **Inertia and Momentum:** In a purely kinematic model, releasing the forward key (`w`) or pressing stop (`s`) would result in the robot stopping instantly. However, in the Gazebo simulation, the robot exhibits inertia. When the stop command is issued, the robot carries forward momentum and "drifts" a short distance before coming to a complete halt due to the simulated physics (mass and friction).
* **Turning Friction and Slipping:** When executing sharp turns at higher speeds, the simulated wheels exhibit slight slipping on the ground plane. This means the robot's heading does not change as perfectly or sharply as the control inputs suggest.
* **Odometry Drift:** While moving, the calculated odometry (estimated via wheel encoders and IMU) slowly accumulates small errors compared to the robot's true position in the simulation. This highlights the importance of the SLAM algorithm (Cartographer), which actively corrects these odometry errors by matching the LiDAR scan data against the known map.
