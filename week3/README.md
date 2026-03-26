Week 3 Lab: ROS 2 Workspace, Turtlesim Patterns, and Multi-Node Execution

Description
This repository contains the deliverables for the Week 3 Mobile Robotics Lab. The objectives were to set up a fresh ROS 2 Humble workspace from scratch, create a new package (`my_turtle_package`) with `rclpy` and `turtlesim` dependencies, and write Python nodes to control the turtles. The final execution demonstrates three independent nodes controlling three separate turtles simultaneously to draw a circle, a square, and a triangle.

Step 1: Workspace Initialization
First, a clean ROS 2 workspace was created and built:

	mkdir -p ~/ros2_ws/src
	cd ~/ros2_ws
	colcon build
	source install/setup.bash

Step 2: Package Creation

A new Python-based package was generated inside the src directory with the necessary dependencies for the simulation:
	cd ~/ros2_ws/src
	ros2 pkg create --build-type ament_python --dependencies rclpy turtlesim --node-name my_node my_turtle_package

Step 3: Node Implementation

Three separate Python scripts were created inside ~/ros2_ws/src/my_turtle_package/my_turtle_package/ to handle the unique movement patterns. Each node was assigned a specific turtle topic to prevent command overlapping:

    circle_turtle.py: Publishes constant linear and angular velocity to /turtle1/cmd_vel.

    square_turtle.py: Publishes a sequence of straight driving and precise 90∘ (π/2 radians) turns to /turtle2/cmd_vel.

    triangle_turtle.py: Publishes a sequence of straight driving and 120∘ (2π/3 radians) turns to /turtle3/cmd_vel.

Step 4: Registration and Building

The executables were registered in the package's setup.py file under console_scripts:
entry_points={
    'console_scripts': [
        'circle_node = my_turtle_package.circle_turtle:main',
        'square_node = my_turtle_package.square_turtle:main',
        'triangle_node = my_turtle_package.triangle_turtle:main',
    		],
	},
The workspace was then recompiled to lock in the new nodes:

	cd ~/ros2_ws
	colcon build
	source install/setup.bash

Step 5: Simulation and Execution

To run the full demonstration, the following sequence was executed across multiple terminals:

Start Simulator: ros2 run turtlesim turtlesim_node

Spawn Turtles: Used the rqt Service Caller plugin to call /spawn and create turtle2 and turtle3 at different starting coordinates.

Run Nodes: Executed the three independent nodes simultaneously in separate sourced terminals:

        ros2 run my_turtle_package circle_node

        ros2 run my_turtle_package square_node

        ros2 run my_turtle_package triangle_node

Problems Faced and Solutions

Problem: Initially, the turtles drawing the square and triangle were suffering from accumulation error (drifting) and the shapes were becoming thicker with each lap because the angle estimates (e.g., 1.57 for 90 degrees) were not precise enough.
Solution: I imported Python's math library and replaced the hardcoded decimal estimates with exact radian calculations (e.g., math.pi / 2.0 for the square and 2.0 * math.pi / 3.0 for the triangle). This eliminated the drift and resulted in perfectly overlapping geometry.

Problem: rqt_graph was only showing one active node, even though multiple shapes were being drawn.
Solution: I realized the graph requires a manual refresh, and that all three terminal windows needed to be actively running their respective ros2 run commands concurrently to map the full network topology.
Reflection

This lab was an excellent deep dive into the truly distributed nature of ROS 2. By separating the circle, square, and triangle logic into three distinct nodes, I gained a much clearer understanding of how ROS 2 handles parallel processing and topic management. It was incredibly satisfying to use rqt to spawn the turtles and watch all three independent scripts execute simultaneously in the same simulation environment without interfering with one another. Learning to troubleshoot the open-loop accumulation error using precise math libraries was also a valuable lesson in mechatronics control design. These modular programming skills are definitely going to be essential for handling multi-sensor integration on real-world robots.
