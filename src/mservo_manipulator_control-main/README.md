# mservo_manipulator_control
   
> Ubuntu 18.04 LTS 환경에서 개발   
   
## message   
> **mservo_msg** : mservo lab에서 사용하는 ros msgs   

## EtherCAT   
> xenomai, soem 필요   
> xenomai의 경우 version 3으로 설치했었다.  
> SOEM   
> ```   
> $ sudo apt install ros-<DISTRO>-soem   
> ```   
> 사용 시 ecat_ifname 항상 확인..   
> dualarm 사용 시 junction 사용, 배터리 항상 확인 필요
   
> **ethercat_test**   
> 관리자 권한 터미널  (sudo -s) 에서 실행   
>   --> 다음과 같이 설치하면 그냥 실행가능하다고 하는데 안해봄   
>   ```
>   $ sudo apt install ros-<DISTRO>-ethercat-ethercat_grant   
>   ```   
>   launch 파일 작성하여 <node> 태그 안에   
>    launch-prefix="ethercat_grant"   
      
>   참고 : https://github.com/orocos/soem   
> - ecat_profile_pos_1.cpp,ecat_profile_pos_2.cpp,mani_ecat_homing.cpp : junction 없이 사용
> - dualarm_ecat_ctrl.cpp 사용 시 wheel과 함께 사용 가능   
> - dualarm_ecat_ctrl_j.cpp 220528 일자 마지막 실험 시 사용한 최종본   
> - dualarm_ecat_ctrl_j_traj.cpp 220608 일자 control_msgs/FollowJointTrajectoryActionGoal type topic을 받을 시 waypoint 사이의 trajectory를 그려 position 제어하는 node   
     
> **참고**    
> * ethtool parameter persist 변경 방법       
> ```    
> $ cd /etc/NetworkManager/dispatcher.d    
> $ sudo nano 20-ethtool    
> ```    
> ```    
> #!/bin/bash    
> /sbin/ethtool -C eno1 rx-usecs 0    
> ```    
> ```      
> $ sudo chmod +x 20-ethtool    
> $ reboot    
> ```    
> * lan port를 찾지 못하는 경우
> ```
> $ sudo nano /etc/netplan/*.ymal    
> ```    
> 내에 네트워크를 추가한다    
> ```    
> network:    
>   ethernets:    
>      eno1:    
>         dhcp4:yes    
>         dhcp6:yes (안해도됨)    
> ```    
> ```    
> $ sudo netplan apply        
> ```    
> ifconfig 명령을 통해 적용된 내용확인   
   

## Gazebo & MoveIt   
   
> **dualarm_config** : solidworks로 만든 urdf 파일과 mesh 파일 (STL)   
>
> * 아래 moveit 패키지 만들 시 urdf가 수정됨
> * urdf 생성 시 dualarm으로 바로 생성되지 않아 ver1/ver2 각각 urdf 생성 후 파일 수정하여 base link에 연결   
>    --> ver1,ver2,gripper 모두 2022/06/08 version으로 업데이트 됨   
> * dummy link, joint를 생성하여야 moveit에서 vurtual joint 활용하여 world에 attatch 가능   
> * griper 끝을 eef position으로 planning 하기 위해서는 urdf 생성 시 eef joint coordinate를 원하는 위치에 생성해야 함   
>
>     
> ver2. limit   
> joint 4 : +- 120   
> joint 5 : +- 130   
>
> joint 6만 CCW가 + 방향 이므로 작동 시 확인 바람   
   
   
> **dualarm_moveit** : dualarm_config로 moveit_setup_assistant 이용해서 생성된 패키지   
>   
> * setup assistant에서 manipulator뿐 아니라 eef 그룹 또한 생성 필요 (현재는 manipulator 마지막 링크와 solid 그리퍼로만 생성)   
> * config 폴더 및 launch 폴더의 파일 수정 필요   
>   
> -> config 폴더 내 파일 수정내역   
> dualarm.rviz : bringup_rviz launch 시 초기화면 설정을 위한 rviz config 파일, rviz에서 다른이름 저장으로 생성   
> dualarm_controllers.yaml : MoveIt에서 불러오는 controller list를 제공하기 위해 생성   
> (controller의 name과 action_ns가 gazebo가 받는 topic과 일치할 수 있도록 작성)
> gazebo_joint_states.yaml : joint_state를 publish하기 위해 생성   
> ros_contollers.yaml : gazebo와 ros_control을 위해 MoveIt에서 생성된 파일 수정   
> (MoveIt controller != ros_control controller 이므로 yaml 파일을 두개로 나누어 사용(dualarm/ros controllers.yaml))   
>   
> -> launch 폴더 내 파일 수정내역   
> dualarm_bringup_gazebo.launch : gazebo 활용 위해 생성   
> dualarm_bringup_rviz.launch : rviz 활용 위해 생성   
> dualarm_moveit_controller_manager.launch : dualarm_controllers.yaml 참조 위해 수정  
> (joint_controller_spawner의 ns가 urdf의 gazebo library 캡션 내의 ns와 같은지 확인 필요. Controller Spawner couldn't find the expected controller_manager ROS interface error 해결)   
> gazebo_states.launch : gazebo_joint_states.yaml 참조 및 robot state publisher 위해 생성   
>  (controller_spawner와 joint_controller_spawner의 namespace가 같은지 확인 필요. )
> moveit_rviz.launch : defalt rviz config 파일 경로 수정   
> planning_context.launch : srdf파일 추가 (rviz planning scene error 해결)   
> ros_controllers.launch : 내용 잘 맞는지 확인
>   
> -> execution order
>   
> terminal1   
> ```
> $ roslaunch dualarm_moveit dualarm_bringup_gazebo.launch   
> ```
> terminal2   
> ```
> $ roslaunch dualarm_moveit dualarm_bringup_rviz.launch   
> ```   
> gazebo launch 시 'position_controllers/JointTrajectoryController' does not exist. 에러가 날 경우 다음 설치   
> ```   
> $ sudo apt-get install ros-melodic-joint-trajectory-controller   
> ```   
> position controller에서 joint trajectory controller가 없어서 그런 것이다.   
   

 
   
> **move_robot** : c++/c/python 이용해서 매니퓰레이터 제어하는 코드 모음  
> - dualarm_test.py : 플래그 없이   
> - dualarm_test_coop.py : 5차년도 최종 시연시 플래그 사용하여 진행한 내용, gqcnn 함께 쓸 시 아래 참조   
> - payload_test.py, repeatability_test.py : 과제 정량적 성능평가를 위한 테스트용   
> - gqcnn.py, gqcnn_crop_resize.py : 물체검출 시스템을 사용하기 위한 코드파일   
>    gqcnn 사용 시 pixel과 실제 크기 (mm) 단위 맞추기, 로봇 베이스로부터의 상대 위치 맞추기 위해 calibration 필요   
>    realsense-viewer 실행하여 카메라 원점 찾고 50mm당 몇 pixel인지 기록   
>    resizing하는 비율 반영하여 계산 --> dualarm_test,dualarm_test_coop 파일 내에 
      

> **참고**   
>   https://github.com/eYSIP-2017/eYSIP-2017_Robotic_Arm/wiki/Interfacing-MoveIt%21-with-Gazebo    
>   https://answers.ros.org/question/214712/gazebo-controller-spawner-warning/    
>   http://gazebosim.org/tutorials/?tut=ros_control

## GQCNN  
   
> realsense D435i와 함께 활용
> 가장 먼저 도커 설치   
> 그리고 user에게 권한 부여 후 "재부팅"   
> ```   
> $ sudo usermod -a -G docker $USER   
> ```   
> (해놓지 않으면 컨테이너 실행 시 docker.sock connect시 permission denied 에러 메세지가 뜰 수 있다)   
> 압축파일 내 docker.sh 실행시켜 컨테이너 생성  
> example.py 실행하여 작동 확인   
> 컨테이너가 죽을 시 (재부팅 등으로 인해) 다시 실행 필요   
> 죽어있는지 확인 방법   
> ```   
> $ docker ps -a   
> ```   
> 컨테이너 다시 실행   
> ```   
> $ docker start gqcnn   
> ```   
> realsense 연결 후 노드 켜기   
> ```   
> $ roslaunch realsense2_camera rs_camera.launch   
> ```   
> 그리고 move_robot 패키지의 dualarm_test.py 또는 dualarm_test_coop.py 실행   


## Gripper  
   
> dynamixel로 만든 1DOF gripper position 제어     
> service 활용함 -> gripper_dist_1,2 0.05   
> dynamixel ID, port number 항상 확인    
>     
> * dxl_gripper_ctrl.py : 두 개의 그리퍼를 하나의 USB port 활용    
> * dxl_gripper_ctrl1.py, dxl_gripper_ctrl2.py : 각 그리퍼당 하나의 USB port, 총 2개 활용    
> * roslaunch dxl_gripper gripper.launch --screen : ctrl1,ctrl2 node 두개 동시에 킴    
