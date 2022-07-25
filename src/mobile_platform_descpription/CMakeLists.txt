cmake_minimum_required(VERSION 2.8.3)

project(mobile_platform_description)

find_package(catkin REQUIRED COMPONENTS
  message_generation
  roscpp
  sensor_msgs
  geometry_msgs
  std_msgs
)

add_message_files(
  FILES
  JointState.msg
)

generate_messages(DEPENDENCIES std_msgs)

catkin_package(   
  LIBRARIES mobile_platform_description
  CATKIN_DEPENDS
   sensor_msgs
   geometry_msgs
   std_msgs
 )




find_package(catkin REQUIRED COMPONENTS
  message_generation
  roscpp
)



find_package(roslaunch)

include_directories(
 # include
  ${catkin_INCLUDE_DIRS}
)


foreach(dir config launch meshes urdf)
	install(DIRECTORY ${dir}/
		DESTINATION ${CATKIN_PACKAGE_SHARE_DESTINATION}/${dir})
endforeach(dir)
