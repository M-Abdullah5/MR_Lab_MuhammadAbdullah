Total of 3 tasks were done, that includes: reset service call, /spawn service call, and control of the second turtle, all using terminal in linux with ros2 installed.
First of all, turtlesim library is installed by: sudo apt install ros-humble-turtlesim
Then it is lauched by command: ros2 run turtlesim turtlesim_node
Entering this opens a separate window with a turtle on it.
Another command to move turtle on square path must be executed on a seperate terminal: ros2 run turtlesim draw_square
Now that turtle would start moving on a square path
The position can be observed using a command on the separate terminal: ros2 topic echo /turtle1/pose
Now to reset, spawn and control of the second terminal, we need to access RQT window that is accessed by a command on the separate terminal: rqt
(Optional) If rqt is not installed, install it using command: sudo apt install ros-humble-rqt
As rqt is opened, node graph can be accessed from the plugins tab above the main working space
There is a service caller that can be accessed from plugins as well, this provides services like reset and spawn
Reset functionality is accessed by selecting /reset service in service caller and then pressing call. This will reset the turtle movements to zero.
Selecting /spawn will let user spawn another turtle on the desired location. Values of x, y, theta and name of the topic is selected, then pressed call to spawn the turtle on the location
Now to control this spawned turtle, go to plugins menu again and find message publisher
Select parameter events in topic and type and press plus button, result should be like: /turtle1/cmd_vel
Here, turtle1, turtle2 are topic names that could be customized and more than 2
Click the arrow besides it to open its properties that includes linear and angular x, y and z
Values can be changed of a turtle as desired and after selecting values, check the box of that turtle for it to start moving on that window with selected parameters
In the window, two turtles can be seen, one moving on a square path and other on a circular path of which parameters we just set.

Observation: Using the rqt interface, we can spawn and control those turtle and had an understanding of using basic rqt. We can control fixed robotics paths independent to each other. RQT provides the best interface to the user by letting it to select many different options by providing a simple GUI.
