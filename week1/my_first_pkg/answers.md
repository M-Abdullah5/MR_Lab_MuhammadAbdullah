1. Define: node, topic, package, workspace. Provide one sentence each. 

    Node: A process that performs computation, such as a controller, sensor driver, or planner.

    Topic: A named communication channel used for streaming messages between nodes.

    Package: A folder containing ROS 2 code, dependencies, and build information.

    Workspace: A directory that contains one or more ROS 2 packages along with their build outputs.

2. Explain why sourcing is required. What happens if you do not source a workspace? 

    Sourcing is required to add the ROS 2 installation and your locally built packages to the terminal's environment. If you do not source a workspace, the terminal will not recognize ROS 2 command , nor will it be able to locate custom packages and executables.

3. What is the purpose of colcon build? What folders does it generate? 

    The purpose of colcon build is to compile the source code and build the packages within your workspace. After building, it generates the build/, install/, and log/ folders alongside the  existing src/ folder.

4. In your own words, explain what the entry_points console script does in setup.py. 

    The entry_points console script registers your Python executable so that ROS 2 knows exactly which Python function to run when a specific command name is called via ros2 run.

5. Draw (by hand or ASCII) a diagram showing one publisher and one subscriber connected by a topic. 
Plaintext

+--------------------+                  +-----------------------+
|      Node A        |                  |        Node B         |
|   (Publisher)      |                  |     (Subscriber)      |
|                    |                  |                       |
| publishes Twist msgs |  /cmd_vel topic  | receives Twist msgs   |
| at 10 Hz           +----------------->| and acts on them      |
+--------------------+                  +-----------------------+
