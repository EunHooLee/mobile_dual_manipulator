# mobile_dual_manipulator
Mservo Lab project


### Example
Execute this command to view the mobile platform and dual arm combination model in the Gazebo envrironment:
```
roslaunch dualarm_moveit dualarm_bringup_gazebo.launch
```
Execute the command below to run rviz for robot path planning
```
roslaunch dualarm_moveit dualarm_bringup_rviz.launch 
```
If rviz is on, make sure that fixed frame is world, and if or not, change it to **"world"**. A world frame is a coordinate of the root link defined in the .urdf file as a **"world link"**. 

For now, the robot is capable of translational motion on the x and y axis and rotational motion on the z-axis in terms of the **world frame**.

### Problems





The joint-link structure is as follows.
**world - virtual_joint (fixed) - world (link) - dummy_joint_x (fixed) - dummy_link - dummy_joint (prismatic x) - dummy_link_1 - dummy_joint_1 (prismatic y) - dummy_link_2 - dummy_joint_2 (revolute z) - base_link**