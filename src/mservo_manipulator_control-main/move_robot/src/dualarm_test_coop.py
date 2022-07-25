#!/usr/bin/env python
import os.path as path
import sys
import copy
import rospy, rospkg

import moveit_commander
import moveit_msgs.msg
import tf
import scipy

from std_msgs.msg import String
from std_msgs.msg import Int8
from sensor_msgs.msg import Image
import geometry_msgs.msg
from dxl_gripper.srv import GripperDist, GripperDistResponse
from moveit_commander.conversions import pose_to_list
from scipy.spatial.transform import Rotation as R
from gqcnn import calc_grasping_point
from gqcnn_crop_resize import crop_and_resize

from math import pi
import numpy as np
from matplotlib import pyplot as plt
import cv2
import time

## END_SUB_TUTORIAL

ERROR = -1
INACTIVE = 0
ACTIVE = 1
SUCCESS = 2

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

    moveit_commander.roscpp_initialize(sys.argv)
    # rospy.init_node('dualarm_'+robot_name, anonymous=True)
    rospy.init_node('dualarm_manipulator', anonymous=True)
    self.listener = tf.TransformListener()

    # scheduler flag
    self.flag = INACTIVE
    self.flag_pub = rospy.Publisher('/manipulator_task_flag', Int8, queue_size=1)
    self.flag_sub = rospy.Subscriber('/manipulator_task_flag', Int8, self.flagCallback)
    
    robot = moveit_commander.RobotCommander()

    scene = moveit_commander.PlanningSceneInterface()
    self.scene = scene


    group_name = robot_name
    self.robot_name = robot_name
    move_group = moveit_commander.MoveGroupCommander(group_name)
    # move_group.set_planning_time(10)


    ## Create a `DisplayTrajectory`_ ROS publisher which is used to display
    ## trajectories in Rviz:
    display_trajectory_publisher = rospy.Publisher('/move_group/display_planned_path',
                                                   moveit_msgs.msg.DisplayTrajectory,
                                                   queue_size=20)

  
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

    move_group.stop()


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


    move_group.set_max_velocity_scaling_factor(0.5)

    move_group.go(joint_goal, wait=True)

    move_group.stop()

    current_joints = move_group.get_current_joint_values()
    return all_close(joint_goal, current_joints, 0.01)

  def set_pose_goal(self, pose):

    move_group = self.move_group

    pose = list(np.copy(pose))

    for i in range(3):
      pose[i] /= 1000.0
    print(pose)
    move_group.set_pose_target(pose)

    plan = move_group.go(wait=True)

    move_group.stop()

    move_group.clear_pose_targets()

    current_pose = self.move_group.get_current_pose().pose
    return True



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

    wpose.position.z += scale * 0.03
    waypoints.append(copy.deepcopy(wpose))
    wpose.position.z += scale * 0.03
    waypoints.append(copy.deepcopy(wpose))


    (plan, fraction) = move_group.compute_cartesian_path(
                                       waypoints,   
                                       0.0005,        
                                       0.0)         
    move_group.execute(plan, wait=True)
    return plan, fraction

  def plan_cartesian_path9(self, scale=1):

    move_group = self.move_group
    move_group.set_max_velocity_scaling_factor(0.4)
    waypoints = []

    wpose = move_group.get_current_pose().pose

    wpose.position.z -= scale * 0.036
    waypoints.append(copy.deepcopy(wpose))

    (plan, fraction) = move_group.compute_cartesian_path(
                                       waypoints,   
                                       0.0005,        
                                       0.0)         
    move_group.execute(plan, wait=True)
    return plan, fraction


  def plan_cartesian_path8(self, scale=1):

    move_group = self.move_group
    move_group.set_max_velocity_scaling_factor(0.4)
    waypoints = []

    wpose = move_group.get_current_pose().pose

    wpose.position.z -= scale * 0.025
    waypoints.append(copy.deepcopy(wpose))


    (plan, fraction) = move_group.compute_cartesian_path(
                                       waypoints,   
                                       0.0005,        
                                       0.0)         
    move_group.execute(plan, wait=True)
    return plan, fraction

  def plan_cartesian_path11(self, scale=1):

    move_group = self.move_group
    move_group.set_max_velocity_scaling_factor(0.4)
    waypoints = []

    wpose = move_group.get_current_pose().pose

    wpose.position.y -= scale * 0.02
    waypoints.append(copy.deepcopy(wpose))


    (plan, fraction) = move_group.compute_cartesian_path(
                                       waypoints,   
                                       0.0005,        
                                       0.0)         
    move_group.execute(plan, wait=True)
    return plan, fraction

  def plan_cartesian_path12(self, scale=1):

    move_group = self.move_group
    move_group.set_max_velocity_scaling_factor(0.4)
    waypoints = []

    wpose = move_group.get_current_pose().pose

    wpose.position.y -= scale * 0.02
    waypoints.append(copy.deepcopy(wpose))


    (plan, fraction) = move_group.compute_cartesian_path(
                                       waypoints,   
                                       0.0005,        
                                       0.0)         
    move_group.execute(plan, wait=True)
    return plan, fraction

  def plan_cartesian_path13(self, scale=1):

    move_group = self.move_group
    move_group.set_max_velocity_scaling_factor(0.4)
    waypoints = []

    wpose = move_group.get_current_pose().pose

    wpose.position.z -= scale * 0.07
    waypoints.append(copy.deepcopy(wpose))


    (plan, fraction) = move_group.compute_cartesian_path(
                                       waypoints,   
                                       0.0005,        
                                       0.0)         
    move_group.execute(plan, wait=True)
    return plan, fraction

  def plan_cartesian_path14(self, scale=1):

    move_group = self.move_group
    move_group.set_max_velocity_scaling_factor(0.4)
    waypoints = []

    wpose = move_group.get_current_pose().pose

    wpose.position.x += scale * 0.04
    waypoints.append(copy.deepcopy(wpose))


    (plan, fraction) = move_group.compute_cartesian_path(
                                       waypoints,   
                                       0.0005,        
                                       0.0)         
    move_group.execute(plan, wait=True)
    return plan, fraction

  def plan_cartesian_path16(self, scale=1):

    move_group = self.move_group
    move_group.set_max_velocity_scaling_factor(0.4)
    waypoints = []

    wpose = move_group.get_current_pose().pose

    wpose.position.x += scale * 0.4
    waypoints.append(copy.deepcopy(wpose))


    (plan, fraction) = move_group.compute_cartesian_path(
                                       waypoints,   
                                       0.0005,        
                                       0.0)         
    move_group.execute(plan, wait=True)
    return plan, fraction

  def plan_cartesian_path15(self, scale=1):

    move_group = self.move_group
    move_group.set_max_velocity_scaling_factor(0.4)
    waypoints = []

    wpose = move_group.get_current_pose().pose

    wpose.position.x -= scale * 0.007
    waypoints.append(copy.deepcopy(wpose))


    (plan, fraction) = move_group.compute_cartesian_path(
                                       waypoints,   
                                       0.0005,        
                                       0.0)         
    move_group.execute(plan, wait=True)
    return plan, fraction

  def plan_cartesian_path20(self, scale=1):

    move_group = self.move_group
    move_group.set_max_velocity_scaling_factor(0.4)
    waypoints = []

    wpose = move_group.get_current_pose().pose

    wpose.position.z -= scale * 0.04
    waypoints.append(copy.deepcopy(wpose))


    (plan, fraction) = move_group.compute_cartesian_path(
                                       waypoints,   
                                       0.0005,        
                                       0.0)         
    move_group.execute(plan, wait=True)
    return plan, fraction


    move_group.execute(plan, wait=True)

    return plan, fraction

  def execute_plan(self, plan):
    move_group = self.move_group
    move_group.execute(plan, wait=True)

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
      plt.imsave(self.rospack.get_path('move_robot')+'/src/cip_data/figure_rgb0.png',data)
      self.rgb_trigger = False
    else:
      pass

  def flagCallback(self, msg):
    self.flag = msg.data
  
  def get_tf(self):
    (trans,rot) = self.listener.lookupTransform('mani1_eff', 'dummy_link', rospy.Time(0))
    return (trans,rot)

def main_loop(rgb_path, depth_path, result_path, manipulator1, manipulator2):
  crop_and_resize(rgb_path, depth_path)        
  grasping_point = calc_grasping_point(rgb_path, depth_path, result_path)
  print(grasping_point)
  center = grasping_point['center']
  angle = grasping_point['angle']
  #real_position = np.array([-229.32330827, 11.27819549, 10]) #(x,y) (mm)
  #real_position = np.array([(center[0]-320)/26.6*25, -(center[1]-240)/26.6*25, 10]) #(x,y) (mm)
  real_position = np.array([(center[0]-320)/75*50, -(center[1]-240)/75*50, 10]) #(x,y) (mm)
  print(real_position)

  box_pose = geometry_msgs.msg.PoseStamped()
  box_pose.header.frame_id = "dummy_link"

  box_pose.pose.orientation.w = 1.0
  box_pose.pose.position.z = 0.767
  box_pose.pose.position.y = 0.715
  box_pose.pose.position.x = 0.03
  box_name1 = "Cameracollision"
  manipulator1.scene.add_box(box_name1, box_pose, size=(0.28, 0.25, 0.19))
  manipulator2.scene.add_box(box_name1, box_pose, size=(0.28, 0.25, 0.19))

  box_pose = geometry_msgs.msg.PoseStamped()
  box_pose.header.frame_id = "dummy_link"
  box_pose.pose.orientation.w = 1.0
  box_pose.pose.position.z = 0.4
  box_pose.pose.position.y = 0
  box_name2 = "box"
  manipulator2.scene.add_box("box", box_pose, size=(0.1, 0.1, 1))
  manipulator1.scene.add_box("box", box_pose, size=(0.1, 0.1, 1))
  # quit()

  box_pose = geometry_msgs.msg.PoseStamped()
  box_pose.header.frame_id = "dummy_link"
  box_pose.pose.orientation.w = 1.0
  box_pose.pose.position.z = 0.6
  box_name3 = "boxformani2"
  manipulator2.scene.add_box("boxformani2", box_pose, size=(0.1, 0.5, 1.4))

  box_pose = geometry_msgs.msg.PoseStamped()
  box_pose.header.frame_id = "dummy_link"
  box_pose.pose.orientation.w = 1.0
  box_pose.pose.position.z = 0.4
  box_pose.pose.position.y = 0
  box_name4 = "centerbox"



  # NEW FOR EXPERIMENT 
        
  # parameters
  ydistance = 515
  tf_robot = np.array([0,ydistance,177]) #(x=same,distance between origin of manipulator and camera,height / both +)        
  tool_location = real_position + tf_robot
  tool_depth = np.array([0,0,180])
  adjustment = 10 #height adjustment while grasping tool
  going_up2 = 100 #(tool)
  going_down2 = -200 #(tool)
  box_location = np.array([380,0,200]) #from camera origin
  p_robot_tool3 = [tf_robot[0]+box_location[0], tf_robot[1]+box_location[1], tf_robot[2]+box_location[2], np.pi, 0, np.pi/2] 

  p_robot_tool4 = [tf_robot[0]+box_location[0], tf_robot[1]+box_location[1], tf_robot[2]+box_location[2]+going_down2, np.pi, 0, np.pi/2] 
  

  manipulator1.go_to_home_state()	
  manipulator2.go_to_home_state()
  #manipulator1.gripper_request(0.07)
  print('yeah1')
  #manipulator2.gripper_request(0.07)
  print('yeah2')

  # Before Grasping tool
  p_robot_tool = [tool_location[0], tool_location[1], tool_depth[2]+going_up2, np.pi, 0, np.pi/2] 
  manipulator2.set_pose_goal(p_robot_tool)

  # Moving Downwards to grasp tool
  p_robot_tool_md = [tool_location[0], tool_location[1], tool_depth[2]+adjustment, np.pi, 0, np.pi/2] 
  manipulator2.set_pose_goal(p_robot_tool_md)

#  time.sleep(3)
#  manipulator2.gripper_request(0.01)     
#  time.sleep(3)

  # Move upwards
  p_robot_tool2 = [tool_location[0], tool_location[1], tool_depth[2]+going_up2 , np.pi, 0, np.pi/2] 
  manipulator2.set_pose_goal(p_robot_tool2)
  manipulator2.scene.remove_world_object("boxformani2")
  time.sleep(5)


  mani_goals = np.array([
    [1,-140,8,25,56,8,59,40],   # Mani1 Box handle removal
    [1,-140,8,25,56,8,96,63],   # Mani1 Box handle removal
    ##[1,-141,7,25,83,10,72,59],   # Mani1 Box handle removal Approaching Box (x,y,z=38,43,30.8),
    [1,-139,7,25,72,7,80,66],
    [11,0,0,0,0,0,0,0],  # y direction adjustment  
    [7,0,0,0,0,0,0,0],   # Downwards
##    [15,0,0,0,0,0,0,0],  # x dir
##    [7,0,0,0,0,0,0,0],   # Downwards
    ##[15,0,0,0,0,0,0,0],  # x dir
#    [3,1,0,0,0,0,0,0],   # Grasp   
    ##[1,-138,11,27,53,5,95,65],    # Mani1 Box handle upwards
    [4,0,0,0,0,0,0,0],           # Mani1 Box handle upwards
    [1,-151,22,19,46,11,96,48],   # Mani1 Box cover placing1 
    [16,0,0,0,0,0,0,0],
    ##[16,0,0,0,0,0,0,0],
    ##[1,-150,31,17,56,11,79,44],   # Mani1 Box cover placing2 (56.9,43,27)
    [20,0,0,0,0,0,0,0],
##    [20,0,0,0,0,0,0,0],
##    [20,0,0,0,0,0,0,0],
    [8,0,0,0,0,0,0,0],  #Downwards2
#    [3,1,1,0,0,0,0,0],   # Box Cover Release
    [1,-151,22,19,46,11,96,48],
    ##[1,-151,19,19,50,12,95,45],
    [1,-117,-32,-22,80,34,69,40],
    [1,-117,-32,-22,80,34,35,20],
    [5,0,0,0,0,0,0,0],
    [2,46,73,106,-15,-111,104,32],     # Moving tool to Box
#    [12,0,0,0,0,0,0,0],  # ydir
#    [14,0,0,0,0,0,0,0],  # xdir
    [13,0,0,0,0,0,0,0],  # Downwards
    ##[2,49,79,107,-21,-110,96,29],     # Placing tool inside Box
#    [3,2,1,0,0,0,0,0],     # Tool Release
    [2,46,73,106,-15,-111,104,32],
    [6,0,0,0,0,0,0,0]
  ])
  for i in range(len(mani_goals)):
    if mani_goals[i][0] == 1:
      manipulator1.go_to_state(mani_goals[i][1:]*np.pi/180) 
      time.sleep(12)
    elif mani_goals[i][0] == 2:
      manipulator2.go_to_state(mani_goals[i][1:]*np.pi/180)
      time.sleep(5) 
    elif mani_goals[i][0] == 3: # gripper
      if mani_goals[i][1] == 1: # mani 1
        if mani_goals[i][2] == 0: # close 1
          time.sleep(4)
          manipulator1.gripper_request(0.03)
          time.sleep(4)
        else:
          time.sleep(4)
          manipulator1.gripper_request(0.07)
          time.sleep(4)
      else: # mani 2
        if mani_goals[i][2] == 0: # close 2
          manipulator2.gripper_request(0.02)
          time.sleep(4)
        else: # open 2
          manipulator2.gripper_request(0.07)
          time.sleep(4) 

    elif mani_goals[i][0]==4:
      manipulator1.plan_cartesian_path10()
      time.sleep(1)
    elif mani_goals[i][0]==5:
      manipulator1.go_to_home_state()
      manipulator1.scene.remove_world_object("box")
      time.sleep(1) 
      manipulator2.scene.remove_world_object("box") 
      manipulator2.scene.add_box("centerbox", box_pose, size=(0.1, 0.05, 1))
    elif mani_goals[i][0]==6:
      box_pose = geometry_msgs.msg.PoseStamped()
      box_pose.header.frame_id = "dummy_link"
      box_pose.pose.orientation.w = 1.0
      box_pose.pose.position.z = 0.4
      box_pose.pose.position.y = 0
      box_pose.pose.position.x = 0.235
      box_name5 = "lastbox"

      manipulator2.scene.add_box("lastbox", box_pose, size=(0.25, 0.4, 1))
      manipulator2.go_to_home_state()
      manipulator2.scene.remove_world_object("centerbox")  
      manipulator2.scene.remove_world_object("lastbox")
      manipulator2.scene.remove_world_object("boxformani3")
      manipulator1.scene.remove_world_object("Cameracollision")
      manipulator2.scene.remove_world_object("Cameracollision")
    elif mani_goals[i][0]==7:
      manipulator1.plan_cartesian_path9()
      time.sleep(2) 
    elif mani_goals[i][0]==8:
      manipulator1.plan_cartesian_path8()
      time.sleep(1) 
    elif mani_goals[i][0]==11:
      manipulator1.plan_cartesian_path11()
      time.sleep(1)    
    elif mani_goals[i][0]==12:
      manipulator2.plan_cartesian_path12() 
      time.sleep(2) 
    elif mani_goals[i][0]==13:
      manipulator2.plan_cartesian_path13()
      time.sleep(2) 
    elif mani_goals[i][0]==14:
      manipulator2.plan_cartesian_path14()
      time.sleep(2) 
    elif mani_goals[i][0]==16:
      manipulator1.plan_cartesian_path16()
      time.sleep(2) 
    elif mani_goals[i][0]==15:
      manipulator1.plan_cartesian_path15()
      time.sleep(2)
    elif mani_goals[i][0]==20:
      manipulator1.plan_cartesian_path20()
      time.sleep(2)
    else:
      pass

#  flag_msg = Int8()	
#  flag_msg.data = SUCCESS
#  manipulator2.flag_pub.publish(flag_msg)

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
    manipulator = False
    if manipulator:
      raw_input()

    else:
      print("hi")
      rgb_path = manipulator1.rospack.get_path('move_robot')+'/src/cip_data/figure_rgb0.png'
      depth_path = manipulator1.rospack.get_path('move_robot')+'/src/cip_data/figure_depth0.npy'

      result_path = manipulator1.rospack.get_path('move_robot')+'/src/cip_data/results'
      time.sleep(0.5)


      (trans, rot) = manipulator2.get_tf()
      print(rot)
      r = R.from_quat(rot)
      print(r.as_euler('zyx')) # [-yaw,-pitch,-roll]


#        if path.isfile(rgb_path) and path.isfile(depth_path) and manipulator2.flag==ACTIVE:
      if path.isfile(rgb_path) and path.isfile(depth_path):
          main_loop(rgb_path, depth_path, result_path, manipulator1, manipulator2)
      else:
          rospy.sleep(0.1)
          


    print( "============ Python tutorial demo complete!")
  except rospy.ROSInterruptException:
    return
  except KeyboardInterrupt:
    return

if __name__ == '__main__':
  main()
