#!/usr/bin/env python
import os.path as path
import sys
import copy
import rospy, rospkg

import moveit_commander
import moveit_msgs.msg
import shape_msgs.msg
import tf
import scipy

from std_msgs.msg import String
from sensor_msgs.msg import Image
import geometry_msgs.msg
from dxl_gripper.srv import GripperDist, GripperDistResponse
from moveit_commander.conversions import pose_to_list
#from scipy.spatial.transform import Rotation as R
from gqcnn import calc_grasping_point
from gqcnn_crop_resize import crop_and_resize

from math import pi
import numpy as np
from matplotlib import pyplot as plt
import cv2
import time

## END_SUB_TUTORIAL


def all_close(goal, actual, tolerance):
  """
  Convenience method for testing if a list of values are within a tolerance of their counterparts in another list
  @param: goal       A list of floats, a Pose or a PoseStamped
  @param: actual     A list of floats, a Pose or a PoseStamped
  @param: tolerance  A float
  @returns: bool
  """
  all_equal = True
  if type(goal) is list:
    for index in range(len(goal)):
      if abs(actual[index] - goal[index]) > tolerance:
        return False

  elif type(goal) is geometry_msgs.msg.PoseStamped:
    return all_close(goal.pose, actual.pose, tolerance)

  elif type(goal) is geometry_msgs.msg.Pose:
    return all_close(pose_to_list(goal), pose_to_list(actual), tolerance)

  return True


class MoveGroupPythonIntefaceTutorial(object):
  """MoveGroupPythonIntefaceTutorial"""
  def __init__(self, robot_name):
    super(MoveGroupPythonIntefaceTutorial, self).__init__()
    self.rgb_image_sub = rospy.Subscriber(
          "/camera2/color/image_raw", Image, self._rgb_CB, queue_size=1)
    self.rs_image_sub = rospy.Subscriber(
            "/camera2/depth/image_rect_raw", Image, self._depth_CB, queue_size=1)
    self.rgb_trigger = True
    self.depth_trigger = True
    self.rospack = rospkg.RosPack()

    ## BEGIN_SUB_TUTORIAL setup
    ##
    ## First initialize `moveit_commander`_ and a `rospy`_ node:
    moveit_commander.roscpp_initialize(sys.argv)
    rospy.init_node('move_group_python_interface_tutorial', anonymous=True)
    self.listener = tf.TransformListener()

    ## Instantiate a `RobotCommander`_ object. Provides information such as the robot's
    ## kinematic model and the robot's current joint states
    robot = moveit_commander.RobotCommander()

    ## Instantiate a `PlanningSceneInterface`_ object.  This provides a remote interface
    ## for getting, setting, and updating the robot's internal understanding of the
    ## surrounding world:
    scene = moveit_commander.PlanningSceneInterface()
    self.scene = scene


    ## Instantiate a `MoveGroupCommander`_ object.  This object is an interface
    ## to a planning group (group of joints).  In this tutorial the group is the primary
    ## arm joints in the Panda robot, so we set the group's name to "panda_arm".
    ## If you are using a different robot, change this value to the name of your robot
    ## arm planning group.
    ## This interface can be used to plan and execute motions:

    ################ NOT ROBOT's NAME --> ARM's NAME IN MoveIt  ######################
    ################ I set up this name in MoveIt Setup Assistant ####################
    ################ Not sure but I might modify this name in SRDF files  ############
    # group_name = "arm_ver1"
    # move_group = moveit_commander.MoveGroupCommander(group_name)
    group_name = robot_name
    self.robot_name = robot_name
    move_group = moveit_commander.MoveGroupCommander(group_name)
    # move_group.set_planning_time(10)


    ## Create a `DisplayTrajectory`_ ROS publisher which is used to display
    ## trajectories in Rviz:
    display_trajectory_publisher = rospy.Publisher('/move_group/display_planned_path',
                                                   moveit_msgs.msg.DisplayTrajectory,
                                                   queue_size=20)

    ## END_SUB_TUTORIAL

    ## BEGIN_SUB_TUTORIAL basic_info
    ##
    ## Getting Basic Information
    # ## ^^^^^^^^^^^^^^^^^^^^^^^^^
    # # We can get the name of the reference frame for this robot:
    # planning_frame = move_group.get_planning_frame()
    # print "============ Planning frame: %s" % planning_frame
    #
    # # We can also print the name of the end-effector link for this group:
    # eef_link = move_group.get_end_effector_link()
    # print "============ End effector link: %s" % eef_link

    # We can get a list of all the groups in the robot:
    group_names = robot.get_group_names()
    print( "============ Available Planning Groups:", robot.get_group_names())

    # Sometimes for debugging it is useful to print the entire state of the
    # robot:
    print( "============ Printing robot state")
    print( robot.get_current_state())
    print( "")
    ## END_SUB_TUTORIAL

    # Misc variables
    # self.box_name = ''
    self.robot = robot
    self.scene = scene
    self.move_group = move_group
    self.display_trajectory_publisher = display_trajectory_publisher
    # self.planning_frame = planning_frame
    # self.eef_link = eef_link
    self.group_names = group_names

  def go_to_state(self, joint_goals):

    move_group = self.move_group
    move_group.set_max_velocity_scaling_factor(0.3)
    # left middle side
    joint_goal = move_group.get_current_joint_values()
    for i in range(len(joint_goal)):
      joint_goal[i] = joint_goals[i]
    #move_group.set_max_velocity_scaling_factor(0.4)

    move_group.go(joint_goal, wait=True)

    # Calling ``stop()`` ensures that there is no residual movement
    move_group.stop()

    ## END_SUB_TUTORIAL

    # For testing:
    current_joints = move_group.get_current_joint_values()
    return all_close(joint_goal, current_joints, 0.01)

  def go_to_joint_state4(self):
    move_group = self.move_group

    # left down side
    joint_goal = move_group.get_current_joint_values()
    joint_goal[0] =  pi / 4
    joint_goal[1] = -pi/5
    joint_goal[2] = 0
    joint_goal[3] = pi/3
    joint_goal[4] = 0
    joint_goal[5] = pi / 2.5
    joint_goal[6] = pi / 4
    move_group.set_max_velocity_scaling_factor(0.4)


    move_group.go(joint_goal, wait=True)

    # Calling ``stop()`` ensures that there is no residual movement
    move_group.stop()

    ## END_SUB_TUTORIAL

    # For testing:
    current_joints = move_group.get_current_joint_values()
    return all_close(joint_goal, current_joints, 0.01)

  def go_to_home_state(self):

    move_group = self.move_group


    joint_goal = move_group.get_current_joint_values()
    joint_goal[0] = 0
    joint_goal[1] = 0
    joint_goal[2] = 0
    joint_goal[3] = 0
    joint_goal[4] = 0
    joint_goal[5] = 0
    joint_goal[6] = 0


    # Set Max velocity of this motion
    move_group.set_max_velocity_scaling_factor(0.4)



    move_group.go(joint_goal, wait=True)

    # Calling ``stop()`` ensures that there is no residual movement
    move_group.stop()

    ## END_SUB_TUTORIAL

    # For testing:
    current_joints = move_group.get_current_joint_values()
    return all_close(joint_goal, current_joints, 0.01)

  def set_pose_goal(self, pose):
    # Copy class variables to local variables to make the web tutorials more clear.
    # In practice, you should use the class variables directly unless you have a good
    # reason not to.
    move_group = self.move_group

    ## BEGIN_SUB_TUTORIAL plan_to_pose
    ##
    ## Planning to a Pose Goal
    ## ^^^^^^^^^^^^^^^^^^^^^^^
    ## We can plan a motion for this group to a desired pose for the
    ## end-effector:
    # pose_goal = geometry_msgs.msg.Pose()
    # pose_goal.orientation.w = 1.0
    # pose_goal.position.x = pose[0]
    # pose_goal.position.y = pose[1]
    # pose_goal.position.z = pose[2]

    # move_group.set_pose_target(pose_goal)
    pose = list(np.copy(pose))

    for i in range(3):
      pose[i] /= 1000.0
    print(pose)
    move_group.set_pose_target(pose)


    #move_group.set_max_velocity_scaling_factor(0.2)
    plan = move_group.go(wait=True)

    # Calling `stop()` ensures that there is no residual movement
    move_group.stop()


    # It is always good to clear your targets after planning with poses.
    # Note: there is no equivalent function for clear_joint_value_targets()
    move_group.clear_pose_targets()

    ## END_SUB_TUTORIAL

    # For testing:
    # Note that since this section of code will not be included in the tutorials
    # we use the class variable rather than the copied state variable
    current_pose = self.move_group.get_current_pose().pose
    #return all_close(pose_goal, current_pose, 0.01)
    return True

  def plan_cartesian_path1(self, scale=1):

    move_group = self.move_group

    # Set Max velocity of this motion
    move_group.set_max_velocity_scaling_factor(0.7)


    ## BEGIN_SUB_TUTORIAL plan_cartesian_path
    ##
    ## Cartesian Paths
    ## ^^^^^^^^^^^^^^^
    ## You can plan a Cartesian path directly by specifying a list of waypoints
    ## for the end-effector to go through. If executing  interactively in a
    ## Python shell, set scale = 1.0.
    ##
    waypoints = []        	
    wpose = move_group.get_current_pose().pose

    wpose.position.z -= scale * 0.05 
    waypoints.append(copy.deepcopy(wpose))
    wpose.position.z -= scale * 0.05
    waypoints.append(copy.deepcopy(wpose))


    # We want the Cartesian path to be interpolated at a resolution of 1 cm
    # which is why we will specify 0.01 as the eef_step in Cartesian
    # translation.  We will disable the jump threshold by setting it to 0.0,
    # ignoring the check for infeasible jumps in joint space, which is sufficient
    # for this tutorial.
    (plan, fraction) = move_group.compute_cartesian_path(
                                       waypoints,   # waypoints to follow
                                       0.001,        # eef_step
                                       0.0)         # jump_threshold

    # Note: We are just planning, not asking move_group to actually move the robot yet:


    move_group.execute(plan, wait=True)
    return plan, fraction

  def plan_cartesian_path2(self, scale=1):

    move_group = self.move_group
    move_group.set_max_velocity_scaling_factor(0.4)
    waypoints = []

    wpose = move_group.get_current_pose().pose

    wpose.position.x -= scale * 0.05
    waypoints.append(copy.deepcopy(wpose))
    wpose.position.x -= scale * 0.05
    waypoints.append(copy.deepcopy(wpose))
    wpose.position.y += scale * 0.003
    waypoints.append(copy.deepcopy(wpose))

    wpose.position.z += scale * 0.005
    waypoints.append(copy.deepcopy(wpose))
    wpose.position.x -= scale * 0.005
    waypoints.append(copy.deepcopy(wpose))



    wpose.position.x -= scale * 0.005
    waypoints.append(copy.deepcopy(wpose))

    wpose.position.y += scale * 0.003
    waypoints.append(copy.deepcopy(wpose))
    
    wpose.position.z += scale * 0.005
    waypoints.append(copy.deepcopy(wpose))
    wpose.position.x -= scale * 0.005
    waypoints.append(copy.deepcopy(wpose))

    wpose.position.x -= scale * 0.003
    waypoints.append(copy.deepcopy(wpose))
    wpose.position.x -= scale * 0.003
    waypoints.append(copy.deepcopy(wpose))
    wpose.position.x -= scale * 0.003
    waypoints.append(copy.deepcopy(wpose))
    wpose.position.x -= scale * 0.003
    waypoints.append(copy.deepcopy(wpose))
    wpose.position.x -= scale * 0.003
    waypoints.append(copy.deepcopy(wpose))


    wpose.position.y -= scale * 0.006
    waypoints.append(copy.deepcopy(wpose))
    wpose.position.y -= scale * 0.006
    waypoints.append(copy.deepcopy(wpose))



    (plan, fraction) = move_group.compute_cartesian_path(
                                       waypoints,   
                                       0.0005,        
                                       0.0)         
    move_group.execute(plan, wait=True)
    return plan, fraction

  def plan_cartesian_path3(self, scale=1):

    move_group = self.move_group
    move_group.set_max_velocity_scaling_factor(0.4)
    waypoints = []

    wpose = move_group.get_current_pose().pose

    wpose.position.z += scale * 0.004
    waypoints.append(copy.deepcopy(wpose))
    wpose.position.x += scale * 0.004
    waypoints.append(copy.deepcopy(wpose))
    wpose.position.z += scale * 0.004
    waypoints.append(copy.deepcopy(wpose))
    wpose.position.z += scale * 0.005
    waypoints.append(copy.deepcopy(wpose))
    wpose.position.x += scale * 0.005
    waypoints.append(copy.deepcopy(wpose))
    wpose.position.x += scale * 0.005
    waypoints.append(copy.deepcopy(wpose))
    wpose.position.x += scale * 0.005
    waypoints.append(copy.deepcopy(wpose))
    wpose.position.x += scale * 0.005
    waypoints.append(copy.deepcopy(wpose))

    wpose.position.x += scale * 0.004
    waypoints.append(copy.deepcopy(wpose))
    wpose.position.x += scale * 0.004
    waypoints.append(copy.deepcopy(wpose))
    wpose.position.x += scale * 0.004
    waypoints.append(copy.deepcopy(wpose))
    wpose.position.x += scale * 0.004
    waypoints.append(copy.deepcopy(wpose))
    wpose.position.x += scale * 0.004
    waypoints.append(copy.deepcopy(wpose))

    wpose.position.x += scale * 0.005
    waypoints.append(copy.deepcopy(wpose))
    wpose.position.x += scale * 0.005
    waypoints.append(copy.deepcopy(wpose))
    wpose.position.x += scale * 0.01
    waypoints.append(copy.deepcopy(wpose))
    wpose.position.x += scale * 0.01
    waypoints.append(copy.deepcopy(wpose))
    wpose.position.x += scale * 0.01
    waypoints.append(copy.deepcopy(wpose))
    wpose.position.z += scale * 0.01
    waypoints.append(copy.deepcopy(wpose))
    wpose.position.z += scale * 0.01
    waypoints.append(copy.deepcopy(wpose))
    wpose.position.z += scale * 0.01
    waypoints.append(copy.deepcopy(wpose))
    wpose.position.z += scale * 0.01
    waypoints.append(copy.deepcopy(wpose))
    wpose.position.z += scale * 0.01
    waypoints.append(copy.deepcopy(wpose))
    wpose.position.z += scale * 0.01
    waypoints.append(copy.deepcopy(wpose))
    wpose.position.z += scale * 0.01
    waypoints.append(copy.deepcopy(wpose))
    wpose.position.z += scale * 0.01
    waypoints.append(copy.deepcopy(wpose))
    wpose.position.z += scale * 0.01
    waypoints.append(copy.deepcopy(wpose))

    (plan, fraction) = move_group.compute_cartesian_path(
                                       waypoints,   
                                       0.0005,        
                                       0.0)         
    move_group.execute(plan, wait=True)
    return plan, fraction

  def plan_cartesian_path4(self, scale=1):

    move_group = self.move_group
    move_group.set_max_velocity_scaling_factor(0.4)
    waypoints = []

    wpose = move_group.get_current_pose().pose

    wpose.position.y -= scale * 0.005
    waypoints.append(copy.deepcopy(wpose))
    wpose.position.y -= scale * 0.005
    waypoints.append(copy.deepcopy(wpose))

    (plan, fraction) = move_group.compute_cartesian_path(
                                       waypoints,   
                                       0.0005,        
                                       0.0)         
    move_group.execute(plan, wait=True)
    return plan, fraction

  def plan_cartesian_path10(self, scale=1):

    move_group = self.move_group
    move_group.set_max_velocity_scaling_factor(0.4)
    waypoints = []

    wpose = move_group.get_current_pose().pose

    wpose.position.z += scale * 0.025
    waypoints.append(copy.deepcopy(wpose))
    wpose.position.z += scale * 0.025
    waypoints.append(copy.deepcopy(wpose))
    wpose.position.z += scale * 0.025
    waypoints.append(copy.deepcopy(wpose))

    (plan, fraction) = move_group.compute_cartesian_path(
                                       waypoints,   
                                       0.0005,        
                                       0.0)         
    move_group.execute(plan, wait=True)
    return plan, fraction



  def plan_cartesian_path_out(self, scale=1):

    move_group = self.move_group

    # Set Max velocity of this motion
    move_group.set_max_velocity_scaling_factor(0.1)


    ## BEGIN_SUB_TUTORIAL plan_cartesian_path
    ##
    ## Cartesian Paths
    ## ^^^^^^^^^^^^^^^
    ## You can plan a Cartesian path directly by specifying a list of waypoints
    ## for the end-effector to go through. If executing  interactively in a
    ## Python shell, set scale = 1.0.
    ##
    waypoints = []

    wpose = move_group.get_current_pose().pose
    # wpose.position.z += scale * 0.1  # First move up (z)
    # wpose.position.y += scale * 0.2 # and sideways (y)
    # waypoints.append(copy.deepcopy(wpose))

    wpose.position.y -= scale * 0.07  # Second move forward/backwards in (x)
    # wpose.position.y += scale * 0.1
    waypoints.append(copy.deepcopy(wpose))

    # wpose.position.y -= scale * 0.2 # Third move sideways (y)
    # waypoints.append(copy.deepcopy(wpose))

    # We want the Cartesian path to be interpolated at a resolution of 1 cm
    # which is why we will specify 0.01 as the eef_step in Cartesian
    # translation.  We will disable the jump threshold by setting it to 0.0,
    # ignoring the check for infeasible jumps in joint space, which is sufficient
    # for this tutorial.
    (plan, fraction) = move_group.compute_cartesian_path(
                                       waypoints,   # waypoints to follow
                                       0.005,        # eef_step
                                       0.0)         # jump_threshold

    # Note: We are just planning, not asking move_group to actually move the robot yet:



    move_group.execute(plan, wait=True)

    return plan, fraction

  def execute_plan(self, plan):
    # Copy class variables to local variables to make the web tutorials more clear.
    # In practice, you should use the class variables directly unless you have a good
    # reason not to.
    move_group = self.move_group


    ## BEGIN_SUB_TUTORIAL execute_plan
    ##
    ## Executing a Plan
    ## ^^^^^^^^^^^^^^^^
    ## Use execute if you would like the robot to follow
    ## the plan that has already been computed:
    move_group.execute(plan, wait=True)

    ## **Note:** The robot's current joint state must be within some tolerance of the
    ## first waypoint in the `RobotTrajectory`_ or ``execute()`` will fail
    ## END_SUB_TUTORIAL

  def gripper_request(self, dist):
    if self.robot_name == 'manipulator1':
      rospy.wait_for_service('gripper_dist_1')
      try:
        result = rospy.ServiceProxy('gripper_dist_1', GripperDist)
        ret = result(dist)
        return ret
      except rospy.ServiceException as e:
        print(e)
    else:
      rospy.wait_for_service('gripper_dist_2')
      try:
        result = rospy.ServiceProxy('gripper_dist_2', GripperDist)

        ret = result(dist)
        return ret
      except rospy.ServiceException as e:
        print(e)

  def _depth_CB(self, msg):
    if self.depth_trigger:
      width = msg.width
      height = msg.height
      data = np.fromstring(msg.data,dtype=np.uint16)
      data = np.reshape(data,(height,width))
      #data = np.flip(data,0)
      path = self.rospack.get_path('move_robot')+'/src/cip_data/figure_depth0'
      np.save(self.rospack.get_path('move_robot')+'/src/cip_data/figure_depth0', data)
      plt.imsave(path+".png", data)
      self.depth_trigger = False
    else:
      pass

  def _rgb_CB(self, msg):
    if self.rgb_trigger:
      width = msg.width
      height = msg.height
      data = np.fromstring(msg.data,dtype=np.uint8)
      data = np.reshape(data,(height,width,3))
      # for k in range(int(height/20)):
      #   for l in range(int(width/20)):
      #     for i in range(-2,2):
      #       for j in range(-2,2):
      #         y_coord = 20*k + i
      #         x_coord = 20*l + j
      #         if y_coord >= height or x_coord >= width:
      #           pass
      #         else:
      #           data[y_coord, x_coord] = 0
      # for i in range(-2,2):
      #   for j in range(-2,2):
      #     data[int(height/2)+i, int(width/2)+j][0] = 255
      # print('show')
      # cv2.namedWindow('_rgb_CB', cv2.WINDOW_FREERATIO)
      # cv2.imshow('_rgb_CB', cv2.cvtColor(data, cv2.COLOR_RGB2BGR))
      # cv2.waitKey(int(1000/20))
      #data = np.flip(data,0)
      plt.imsave(self.rospack.get_path('move_robot')+'/src/cip_data/figure_rgb0.png',data)
      self.rgb_trigger = False
    else:
      pass
  
  def get_tf(self):
    (trans,rot) = self.listener.lookupTransform('mani1_eff', 'dummy_link', rospy.Time(0))
    # (trans,rot) = self.listener.lookupTransform('base_footprint', 'map', rospy.Time(0))
    return (trans,rot)

def main():
  try:
    print( "")
    print( "----------------------------------------------------------")
    print( "Welcome to the MoveIt! MoveGroup Python Interface Tutorial")
    print( "----------------------------------------------------------")
    print( "Press Ctrl-D to exit at any time")
    print( "")
    print( "============ Press `Enter` to begin the tutorial by setting up the moveit_commander ...")
    # raw_input()
    manipulator1 = MoveGroupPythonIntefaceTutorial('manipulator1') #right
    manipulator2 = MoveGroupPythonIntefaceTutorial('manipulator2') #left

    print( "============ Press `Enter` to execute a movement using a joint state goal ...")
    manipulator = True
    if manipulator:
      

      joint_goals = np.array([
	[1,-37,-25,-31,76,0,77,-52],        
	[2,-120,15,30,-94,-42,-82,120],     # Moving tool to Box
	[1,0,0,0,0,0,0,0],
	[2,0,0,0,0,0,0,0]
      
      ])

      raw_input()
      manipulator1.go_to_home_state()
      print("done")      

      raw_input()
      manipulator2.go_to_home_state()
      print("done")

      box_pose = geometry_msgs.msg.PoseStamped()
      box_pose.header.frame_id = "mani2_link8"
      box_pose.pose.orientation.w = 1.0
      box_pose.pose.position.z = 0
      box_pose.pose.position.y = 0
      box_pose.pose.position.x = 0
      box_name = "box"
      manipulator2.scene.add_box(box_name, box_pose, size=(0.1, 0.1, 0.1))
      manipulator2.scene.attach_box("mani2_link8",box_name,touch_links = ["mani2_link8"])

      #
      raw_input()
      manipulator2.set_pose_goal([215,446,324,-3,-0.00170,3.02]);
      print("done")

      raw_input()
      manipulator1.go_to_home_state()
      
      manipulator2.scene.remove_attached_object("mani2_link8",box_name)
      # manipulator2.scene.remove_world_object("centerbox")

      print("done")

      raw_input()
      manipulator2.go_to_home_state()
      print("done")

      manipulator2.scene.remove_world_object(box_name)

#      for i in range(len(joint_goals)):
#        raw_input()
#        print(joint_goals[i])
#        if joint_goals[i][0] == 1:

 #         manipulator1.go_to_state(joint_goals[i][1:]*np.pi/180)
#        elif joint_goals[i][0] == 2:
#          manipulator2.go_to_state(joint_goals[i][1:]*np.pi/180)
#        else:
#          pass
#        print("done")

    
      # tutorial.go_to_joint_state3()

      # raw_input()
    else:
      print("hi")
      rgb_path = manipulator1.rospack.get_path('move_robot')+'/src/cip_data/figure_rgb0.png'
      depth_path = manipulator1.rospack.get_path('move_robot')+'/src/cip_data/figure_depth0.npy'
      # txt_path = manipulator1.rospack.get_path('move_robot')+'/src/cip_data/grasping_result0.txt'
      # image_path = manipulator1.rospack.get_path('move_robot')+'/src/cip_data/grasping_result0.jpg'
      result_path = manipulator1.rospack.get_path('move_robot')+'/src/cip_data/results'
      # raw_input()
      time.sleep(0.5)
      # print(manipulator1.move_group.get_current_pose().pose)

      # manipulator1.go_to_home_state()
      #manipulator2.go_to_home_state()
      #(trans, rot) = manipulator2.get_tf()
      #print(rot)
      #r = R.from_quat(rot)
      # print(r.as_euler('xyz'))
      #print(r.as_euler('zyx')) # [-yaw,-pitch,-roll]


      # print(tf.transformations.euler_from_quaternion(manipulator2.get_tf()[1]))
      # manipulator1.go_to_home_state()
      # manipulator1.set_pose_goal([-0.065582, 0.435321, 0.239971, 3.116874, 0, 0]) #horizontal
      # manipulator1.set_pose_goal([-0.065582, 0.435321, 0.239971, 3.116874, 0, np.pi/2]) #vertical, positive = clockwise
      # manipulator1.set_pose_goal([-0.065582, 0.435321, 0.239971, 3.116874, 0, -np.pi/2])
      # manipulator1.set_pose_goal([0.1393,-0.7623,0.5510 ,-1])

      if path.isfile(rgb_path) and path.isfile(depth_path):
	crop_and_resize(rgb_path, depth_path)        
	grasping_point = calc_grasping_point(rgb_path, depth_path, result_path)
        print(grasping_point)
        center = grasping_point['center']
        angle = grasping_point['angle']
        #real_position = np.array([(center[0]-320)/100*95, -(center[1]-240)/100*95, 10]) #(x,y) (mm)
        #real_position = np.array([(center[0]-320)/26.6*25, -(center[1]-240)/26.6*25, 10]) #(x,y) (mm)
        real_position = np.array([(center[0]-320)/(75*0.74)*50, -(center[1]-240)/(75*0.67)*50, 10]) #(x,y) (mm)  /(pixel*resizing factor)*mm
  
        print(real_position)
        # real_position = [0,0,0]
        # angle = 0
      
        # TODO: get mobile robot tf
        # tf_robot = np.array([trans[0],trans[1], 631])
        #tf_robot = np.array([-100,-650, 631])
        # TODO: get p_table (x,y,z)
        # p_table = np.array([235,523,735])
        #p_table = np.array([0,0,735])
        #p_box = np.array([-250,-180, 170])
        #p_maporigin_obj = p_table + real_position

        #p_robot_box = p_table + p_box - tf_robot #[-250, 470, 250]

        box_pose = geometry_msgs.msg.PoseStamped()
        box_pose.header.frame_id = "dummy_link"

        box_pose.pose.orientation.w = 1.0
        box_pose.pose.position.z = 0.777
        box_pose.pose.position.y = 0.635
        box_pose.pose.position.x = 0.04
        box_name = "Cameracollision"
        manipulator1.scene.add_box(box_name, box_pose, size=(0.28, 0.30, 0.16))
        manipulator2.scene.add_box(box_name, box_pose, size=(0.28, 0.30, 0.16))

        box_pose = geometry_msgs.msg.PoseStamped()
        box_pose.header.frame_id = "dummy_link"
        box_pose.pose.orientation.w = 1.0
        box_pose.pose.position.z = 0.4
        box_pose.pose.position.y = 0
        box_name = "box"
        manipulator2.scene.add_box(box_name, box_pose, size=(0.1, 0.1, 1))
        # manipulator1.scene.add_box(box_name, box_pose, size=(0.2, 0.2, 1))
        # quit()

# NEW FOR EXPERIMENT 
        
 	# parameters
	ydistance = 600
	tf_robot = np.array([0,ydistance,177]) #(x=same,distance between origin of manipulator and camera,height / both +)        
	tool_location = real_position + tf_robot
        tool_depth = np.array([0,0,180])
	adjustment = 2 #height adjustment while grasping tool
	going_up2 = 100 #(tool)
	going_down2 = -200 #(tool)
	box_location = np.array([380,0,200]) #from camera origin
        p_robot_tool3 = [tf_robot[0]+box_location[0], tf_robot[1]+box_location[1], tf_robot[2]+box_location[2], np.pi, 0, np.pi/2] 

        p_robot_tool4 = [tf_robot[0]+box_location[0], tf_robot[1]+box_location[1], tf_robot[2]+box_location[2]+going_down2, np.pi, 0, np.pi/2] 
  

	manipulator1.go_to_home_state()
	manipulator2.go_to_home_state()
	#manipulator1.gripper_request(0.08)
        #manipulator2.gripper_request(0.08)

   # Before Grasping tool
        p_robot_tool = [tool_location[0], tool_location[1], tool_depth[2]+going_up2, np.pi, 0, np.pi/2] 
        manipulator2.set_pose_goal(p_robot_tool)

   # Moving Downwards to grasp tool
        p_robot_tool_md = [tool_location[0], tool_location[1], tool_depth[2]+adjustment, np.pi, 0, np.pi/2] 
        manipulator2.set_pose_goal(p_robot_tool_md)
	
        time.sleep(2)

	#manipulator2.gripper_request(0.025)

   # Move upwards
        p_robot_tool2 = [tool_location[0], tool_location[1], tool_depth[2]+going_up2 , np.pi, 0, np.pi/2] 
        manipulator2.set_pose_goal(p_robot_tool2)


      mani_goals = np.array([
        [1,-37,-25,-31,76,0,77,-52],        
	[2,-120,15,30,-94,-42,-82,120]
        #[1,-142,3,21,67,12,90,58],   # Mani1 Box handle removal
        #[1,-140,6,23,81,10,74,59],   # Mani1 Box handle removal Approaching Box (x,y,z=38,43,32.2)
        #[3,1,0,0,0,0,0,0],   #Grasp
        #[4,0,0,0,0,0,0,0],   # Mani1 Box handle upwards
        #[1,-148,21,14,59,13,85,42],   # Mani1 Box cover placing1 
        #[1,-151,34,18,72,10,61,35],    # Mani1 Box cover placing2 (59,43,16.5)
        #[1,-148,21,14,59,13,85,42],
        #[3,1,1,0,0,0,0,0],   # Box Cover Release
        #[5,0,0,0,0,0,0,0],
        #[2,54,72,103,-27,-111,101,29],     # Moving tool to Box
        #[2,51,81,107,-25,-110,92,28],     # Placing tool inside Box
        #[3,2,1,0,0,0,0,0],     # Tool Release
        #[6,0,0,0,0,0,0,0]
	])
      for i in range(len(mani_goals)):
        if mani_goals[i][0] == 1:
	  manipulator1.go_to_state(mani_goals[i][1:]*np.pi/180) 
 	elif mani_goals[i][0] == 2:
            manipulator2.go_to_state(mani_goals[i][1:]*np.pi/180) 
        elif mani_goals[i][0] == 3: # gripper
          if mani_goals[i][1] == 1: # mani 1
            if mani_goals[i][2] == 0: # close 1
              manipulator1.gripper_request(0.03)
            else:
              manipulator1.gripper_request(0.08)
          else: # mani 2
            if mani1_goals[i][2] == 0: # close 2
              manipulator2.gripper_request(0.025)
            else: # open 2
              manipulator2.gripper_request(0.08) 

        elif mani_goals[i][0]==4:
	  manipulator1.plan_cartesian_path10()
        elif mani_goals[i][0]==5:
 	  manipulator1.go_to_home_state() 
        elif mani_goals[i][0]==6:
 	  manipulator2.go_to_home_state() 
        else:
          pass
          








        #p_robot_box_0 = [-310 - tf_robot[0], p_robot_box[1]+25, 150+p_robot_box[2], np.pi, 0, np.pi/2] # lefter outmost
        #manipulator2.set_pose_goal(p_robot_box_0)
        #print("1")
        # time.sleep(1)
        
        #p_robot_box_1 = [p_robot_box[0], p_robot_box[1], 150+p_robot_box[2], np.pi, 0, np.pi/2] # to box_air
        #manipulator2.set_pose_goal(p_robot_box_1)
        # time.sleep(0.5)
        #print("2")

        #p_robot_box_2 = [p_robot_box[0], p_robot_box[1], p_robot_box[2], np.pi, 0, np.pi/2] # to box handle
        #manipulator2.set_pose_goal(p_robot_box_2)
        # time.sleep(0.5)
        # quit()
        #print("3")

        #manipulator2.scene.remove_world_object(box_name)
        
    #    manipulator2.gripper_request(0.007)

        #p_robot_box_1 = [p_robot_box[0], p_robot_box[1], 150+p_robot_box[2], np.pi, 0, np.pi/2]  # to box air (after grasp)
        #manipulator2.set_pose_goal(p_robot_box_1)
        # time.sleep(1)
        #print("4")

        #p_robot_box_0 = [-400 - tf_robot[0], p_robot_box[1], 150+p_robot_box[2], np.pi, 0, np.pi/2] # lefter outmost (after grasp)
        #manipulator2.set_pose_goal(p_robot_box_0)
        # time.sleep(1)
        #print("5")


        #p_robot_obj = p_maporigin_obj - tf_robot
        #print(p_robot_obj)

       # w = -r.as_euler('zyx')[0]
        # w=0

        #p_robot_obj_0 = [350 - tf_robot[0], p_robot_obj[1], 50+p_robot_obj[2], -np.pi,  0, -w-angle] # to righter outmost
        #manipulator1.set_pose_goal(p_robot_obj_0)
        # print(manipulator1.move_group.get_current_joint_values())
      #  time.sleep(1)
        #print("6")

        #p_robot_obj_1 = list(p_robot_obj[:2]) + [50+p_robot_obj[2], -np.pi,  0, -w-angle] # to obj_air
        #manipulator1.set_pose_goal(p_robot_obj_1)
        # print(manipulator1.move_group.get_current_joint_values())
    #    time.sleep(1)
        #print("7")

        #p_robot_obj_2 = list(p_robot_obj) + [-np.pi,  0, -w-angle] # to obj
        #manipulator1.set_pose_goal(p_robot_obj_2)
        # print(manipulator1.move_group.get_current_joint_values())
     #   time.sleep(1)
        #print("8")

     #   manipulator1.gripper_request(0.015)

        # p_robot_obj_1 = list(p_robot_obj[:2]) + [50+p_robot_obj[2], -np.pi,  0, -w-angle] # to obj_air
        # manipulator1.set_pose_goal(p_robot_obj_1)

        # p_robot_obj_3 = np.copy(p_robot_obj_1)
        # p_robot_obj_3[2] = p_robot_box[2] + 10
        # manipulator1.set_pose_goal(p_robot_obj_3)
        # print(manipulator1.move_group.get_current_joint_values())
        if manipulator1.move_group.get_current_joint_values()[0] < 0:
          states = [-0.9595101846605951, 0.26497518660891206, 0.007779192181427419, 1.2694110516302564, 0.09060212369140697, 1.079005502442003, 1.637026607583806]
        else:
          states = [2.179431778683787, -0.7623196054617134, 0.32418525754211824, -0.4371157074048426, -0.24413223310636756, -1.667470072618892, -1.5902639066093958]
        #manipulator1.go_to_state(states)
        time.sleep(1)
        #print("9")

        # manipulator2.scene.remove_world_object(box_name)

        # p_robot_box_1 = [p_robot_box[0], p_robot_box[1]-15, 10+p_robot_box[2], -np.pi, 0, target_angle]  # to box air (after grasp)
        # manipulator1.set_pose_goal(p_robot_box_1)
        # time.sleep(1)
        # print("10")

        # p_robot_box_2 = [p_robot_box[0], p_robot_box[1]+15, -50 + p_robot_box[2], -np.pi, 0, target_angle]  # to box air (after grasp)
        # manipulator1.set_pose_goal(p_robot_box_2)
        # time.sleep(1)
        # print("11")

      #  manipulator1.gripper_request(0.06)        

        # p_robot_box_1 = [p_robot_box[0], p_robot_box[1]+15, 150+p_robot_box[2], -np.pi, 0, target_angle]  # to box air (after grasp)
        # manipulator1.set_pose_goal(p_robot_box_1)
        # # time.sleep(1)
        # print("12")

        #p_robot_obj_0 = [350 - tf_robot[0], p_robot_obj[1]+15, 150+p_robot_obj[2], -np.pi,  0, target_angle] # to righter outmost
        #manipulator1.set_pose_goal(p_robot_obj_0)
        time.sleep(1)
        #print("13")

        manipulator1.go_to_home_state()
        print("-1")
        

        #p_robot_box_1 = [p_robot_box[0], p_robot_box[1], 150+p_robot_box[2], np.pi, 0, np.pi/2]  # to box air (after grasp)
        #manipulator2.set_pose_goal(p_robot_box_1)
        # time.sleep(1)
        #print("15")

        #p_robot_box_2 = [p_robot_box[0], p_robot_box[1], -50 + p_robot_box[2], np.pi, 0, np.pi/2] # to box handle
        #manipulator2.set_pose_goal(p_robot_box_2)
        # time.sleep(1)
        #print("16")

     #   manipulator2.gripper_request(0.07)

        manipulator2.go_to_home_state()

    print( "============ Python tutorial demo complete!")
  except rospy.ROSInterruptException:
    return
  except KeyboardInterrupt:
    return

if __name__ == '__main__':
  main()
