# mobile_dual_manipulator
Mservo Lab project


### Example
Execute this command to view the mobile platform and dual arm combination model in the Gazebo envrironment:
```
roslaunch mobile_platform_description X_main.launch 
```
Execute the command below to run rviz for robot path planning
```
roslaunch dualarm_moveit dualarm_bringup_rviz.launch 
```
If you want to move the mobile platform, you can use the command:
```
rostopic pub /vel geometry_msgs/Twist "linear:
  x: 0.1
  y: 0.0
  z: 0.0
angular:
  x: 0.0
  y: 0.0
  z: 0.0
```
