# mobile_dual_manipulator
Mservo Lab project


### Example
Execute this command to view the mobile platform and dual arm combination model in the Gazebo envrironment:
```
roslaunch dualarm_moveit dualarm_bringup_gazebo.launch
```
Execute the command below to run rviz for whole body control of robot.
```
roslaunch dualarm_moveit dualarm_bringup_rviz.launch 
```
If rviz is on, make sure that fixed frame is world, and if or not, change it to **"world"**. A world frame is a coordinate of the root link defined in the .urdf file as a **"world link"**. 

For now, the robot is capable of translational motion on the x and y axis and rotational motion on the z-axis in terms of the **world frame**.

Please consult the file at the path below if you would want to view the URDF structure.
```
cd ~/catkin_ws/src/mservo_manipulator_control-main/dualarm_config/urdf
code dualarm_urdf.png
```
### Problems
1. 현재는 mobile platform과 left manipulator (manipulator 1)만 연결되어 있어서 whole-body control은 left manipulator만 가능하다. 즉, right manipulator는 mobile platorm과 구분되어 있다.

2. 위와 같이 할수밖에 없는 이유는 URDF structure에서 보면 현재 dummy_joint_l3가 base_link와 연결되어 있는데 양쪽팔 제어를 위해 dummy_link에서 부터 joint 3개(p,p,r)를 추가할 경우 base_link에 두 개의 parants joint (dummy_joint_l3, dummy_joint_r3)가 부착되고 만들어진 URDF 구조를 graph로 추출하면 둘 중 한개의 joint가 사라진 상태로 만들어진다. ( - link는 2개의 parents joint를 갖을 수 없다는 말이 있다.)

3. 또한 현재와 같이 URDF structure를 만들고, dummy_joint_l1, dummy_joint_l2, dummy_joint_l3,를 두 manipulator에서 공유하게 한다면 즉, srdf 파일의 group을 위 joint가 공유된 상대로 mani1, mani2 의 두개의 group을 구성한다면 ..._rviz.launch 파일 실행 시 controller 충돌(?) 오류가 발생했다. 즉, 한개의 controller를 한 group에서만 사용하라는 오류가 발생했다.

4. 마지막으로 애초에 dummy_link에서 부터 병렬적으로(2갈래로) URDF 구조를 구성한다면 또한, base_link 또한 2개로 나눠 구성한다면 결국 base_link1 에 대한 base_link2의 관계를 표현하기 위해 즉, base_link1 이 움직일 때 base_link2 또한 똑같이 움직여야 하므로 이 둘을 어짜피 fixed joint 로 결합해야 한다. 즉, problem 2 와 같은 문제가 발생한다. 결국 어떤 지점에서 두갈래로 나누더라도 나눠진 urdf 갈래를 한번은 결합해야 한다. (mobile robot은 1대이고, 즉, 2대로 분리를 했으면 서로에 대한 위치를 알려줘야 하고 한 좌표계가 움직이면 나머지 한개의 좌표계도 같이 움직여야 하기 때문이다.)

이러한 이유로 완벽한 whole-body control은 아직 성공하지 못했다.



