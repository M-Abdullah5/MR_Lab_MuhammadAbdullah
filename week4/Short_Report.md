Lab Report: Approach, Findings, and Observations

1. Approach
The objective of this lab was to utilize ROS 2 launch files, bag recording, and rqt plotting to manage and observe a multi-node system.

    First, a custom Python package (my_launch_pkg) was created.

    A follower.py node was implemented utilizing a proportional control loop that continuously calculates the Euclidean distance and heading error between turtle1 and turtle2.

    To streamline execution, a ROS 2 launch file (turtlesim_launch.py) was written to boot the simulator and the custom follower node simultaneously. (Note: The keyboard teleop node was run in a separate terminal to prevent background execution crashes).

    Finally, standard ROS 2 CLI commands (ros2 bag record) and GUI tools (rqt_plot) were used to log and visualize the velocity commands in real-time.

2. Findings

    Launch File Efficiency: Using a launch file drastically reduced the overhead of starting complex systems. Instead of sourcing and running multiple independent commands, the entire environment (nodes, parameters, and simulator) initialized from a single terminal prompt.

    Control Loop Instability: During initial testing, the follower node experienced an "Orbit of Death." Because the linear velocity was too high relative to its turning speed, the follower overshot the target and entered an infinite loop of circling the leader.

    Algorithmic Correction: This was resolved by implementing a threshold gate in the logic: the follower was programmed to maximize angular velocity first and only apply linear forward velocity if its heading error was within an acceptable margin (<0.2 radians).

3. Observations

    Visualization Validates Math: Using rqt_plot provided immediate visual confirmation of the mathematical logic. Watching the cmd_vel graph spike and then smoothly curve down to zero perfectly mirrored the proportional error calculation written in the Python script.

    The Importance of Rosbag: Recording the topics via rosbag highlighted how useful historical data logging is. Being able to pause, inspect, and replay the exact commands the system issued is an invaluable debugging tool, proving that ROS 2 can easily simulate real-world flight recorders for autonomous systems.
