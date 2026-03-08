# Week 1 Lab: Linux Onboarding, Workspace Setup, and ROS 2 Node Creation

## Description
This repository contains the deliverables for the Week 1 Mobile Robotics Lab. The primary objectives were setting up a ROS 2 Humble workspace, creating a custom Python package (`my_first_pkg`), and writing a basic executable node (`simple_node`). Three specific tasks were accomplished: 
1. Customizing the node's log message.
2. Implementing a persistent run counter by reading/writing to a text file.
3. Utilizing ROS 2 parameters to pass and print a student name dynamically via the command line.

## Commands Used
Here are the main commands used to build, manage, and run the ROS 2 workspace:
* `mkdir -p ~/ros2_ws_MuhammadAbdullah/src` - Created the workspace directory.
* `cd ~/ros2_ws_MuhammadAbdullah` - Navigated to the root of the workspace.
* `colcon build` - Compiled the packages in the workspace.
* `source install/setup.bash` - Sourced the environment variables to make the packages executable.
* `ros2 pkg create --build-type ament_python my_first_pkg` - Created the Python package.
* `ros2 run my_first_pkg simple_node` - Executed the node for Tasks 1 and 2.
* `ros2 run my_first_pkg simple_node --ros-args -p student_name:="Muhammad Abdullah"` - Executed the node while passing a custom ROS parameter for Task 3.

## Problems Faced and Solutions
**Problem 1:** While building the workspace with `colcon build`, some warning messages stating that the package "doesn't explicitly install a marker in the package index" and "doesn't explicitly install the 'package.xml' file". 
**Solution:** After reviewing the build process, these were standard deprecation warnings related to newer versions of Python's `setuptools` interacting with `colcon`. The build still finished successfully, and the fallback mechanisms handled the installation, so no code changes were strictly necessary.

**Problem 2:** Keeping track of the "Run count" for Task 2.
**Solution:** Normal Python variable couldn't be used because the node restarts completely every time `ros2 run` is called. I solved this by implementing file I/O, writing the counter to a text file in the package directory and reading/updating it on each run.

## Reflection
This first lab provided a solid foundation in ROS 2's distributed architecture, marking a clear shift from standard single-script execution to a modular approach. Setting up the workspace and getting comfortable with Linux terminal navigation are essential stepping steps. I can already see how the node and topic structure will be incredibly useful for our many projects.
