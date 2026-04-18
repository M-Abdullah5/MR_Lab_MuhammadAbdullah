# Deliverable 1: Step-by-Step Task Completion Report
**Lab:** Introduction to Gazebo and RViz with ROS 2 using TurtleBot3

## Steps Executed to Complete Lab Tasks:

**Step 1: Package Installation and Environment Setup**
1. Opened a terminal and refreshed the package index using `sudo apt update` to ensure no stale repository links were used.
2. Installed the required ROS 2 packages using the command: `sudo apt install ros-humble-turtlebot3* ros-humble-gazebo-ros-pkgs`
3. Set the target robot model by executing `export TURTLEBOT3_MODEL=burger`.
4. Sourced the ROS 2 workspace to make the packages available: `source /opt/ros/humble/setup.bash`.

**Step 2: Launching Gazebo Simulation**
1. Encountered a `spawn_entity` error due to a background process. Cleared it by executing `killall -9 gzserver gzclient`.
2. Launched the simulation using: `ros2 launch turtlebot3_gazebo turtlebot3_world.launch.py`.
3. Waited for the Gazebo GUI to load the empty world and spawn the TurtleBot3 burger model.

**Step 3: Initializing SLAM and RViz**
1. Opened a second terminal, sourced the workspace, and exported the model variable.
2. Launched the Cartographer node with simulated time enabled: `ros2 launch turtlebot3_cartographer cartographer.launch.py use_sim_time:=true`.
3. In the RViz interface that opened, changed the `Fixed Frame` to `map`.
4. Clicked the "Add" button and enabled the required visualization plugins: `Map`, `LaserScan`, `TF`, `Odometry`, and `Path`.

**Step 4: Teleoperation, Recording, and Mapping**
1. Opened a third terminal, sourced the environment, and started the keyboard control node: `ros2 run turtlebot3_teleop teleop_keyboard`.
2. Opened a fourth terminal and started recording all topic data using: `ros2 bag record -a`.
3. Used the `w`, `a`, `s`, `d`, and `x` keys to navigate the robot through the Gazebo world to complete the Cartographer map.
4. Drove the robot back to the approximate (0,0,0) starting coordinate.
5. Stopped the bag recording (`Ctrl+C`).
6. Opened a new terminal, created a maps directory (`mkdir ~/maps`), and saved the generated map using: `ros2 run nav2_map_server map_saver_cli -f ~/maps/my_map`.

**Step 5: ROS 2 Scripting (/cmd_vel and /odom)**
1. Created a dedicated directory for the lab scripts: `mkdir -p ~/mct454l_lab5` and navigated into it.
2. Used the nano text editor (`nano velocity_publisher.py`) to create a ROS 2 Node that toggles a `geometry_msgs/msg/Twist` message to the `/cmd_vel` topic every 2 seconds using a timer callback.
3. Verified the `/odom` message type was `nav_msgs/msg/Odometry`.
4. Used nano (`nano odom_subscriber.py`) to create a node subscribing to `/odom` that extracts and prints the `msg.pose.pose.position.x` and `y` coordinates.
5. Ran both scripts in separate terminals using `python3` to verify their functionality and took screenshots of the outputs.
6. Ran `rqt_graph` in a separate terminal to capture the node connections.
