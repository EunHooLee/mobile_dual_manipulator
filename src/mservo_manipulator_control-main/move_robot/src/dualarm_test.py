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
from scipy.spatial.transform import Rotation as R
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
    def __init__(self, robot_name, trigger):
        super(MoveGroupPythonIntefaceTutorial, self).__init__()
        # self.rgb_image_sub = rospy.Subscriber(
        #     "/camera2/color/image_raw", Image, self._rgb_CB, queue_size=1)
        # self.rs_image_sub = rospy.Subscriber(
        #     "/camera2/depth/image_rect_raw", Image, self._depth_CB, queue_size=1)
        if trigger:
            self.rgb_trigger = True
            self.depth_trigger = True
        else:
            self.rgb_trigger = False
            self.depth_trigger = False
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

        # move_group.go(joint_goal, wait=True)
        move_group.set_joint_value_target(joint_goal)
        plan2 = move_group.plan()
        display_trajectory = moveit_msgs.msg.DisplayTrajectory()
        display_trajectory.trajectory_start = self.robot.get_current_state()
        display_trajectory.trajectory.append(plan2)
        self.display_trajectory_publisher.publish(display_trajectory)
        value = raw_input("Replanning? (y/n)")
        while (value != 'n' ):
            plan2 = move_group.plan()
            display_trajectory = moveit_msgs.msg.DisplayTrajectory()
            display_trajectory.trajectory_start = self.robot.get_current_state()
            display_trajectory.trajectory.append(plan2)
            self.display_trajectory_publisher.publish(display_trajectory)
            value = raw_input("Replanning? (y/n)")
        move_group.execute(plan2,wait=True)
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
        move_group.set_joint_value_target(joint_goal)
        # move_group.go(joint_goal, wait=True)
        plan2 = move_group.plan()
        display_trajectory = moveit_msgs.msg.DisplayTrajectory()
        display_trajectory.trajectory_start = self.robot.get_current_state()
        display_trajectory.trajectory.append(plan2)
        self.display_trajectory_publisher.publish(display_trajectory)
        value = raw_input("Replanning? (y/n)")
        while (value != 'n'):
            plan2 = move_group.plan()
            display_trajectory = moveit_msgs.msg.DisplayTrajectory()
            display_trajectory.trajectory_start = self.robot.get_current_state()
            display_trajectory.trajectory.append(plan2)
            self.display_trajectory_publisher.publish(display_trajectory)
            value = raw_input("Replanning? (y/n)")
        move_group.execute(plan2,wait=True)

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
        pose_goal = geometry_msgs.msg.Pose()

        pose_goal.position.x = pose[0]/1000.0
        pose_goal.position.y = pose[1]/1000.0
        pose_goal.position.z = pose[2]/1000.0
        pose_goal.orientation.x = pose[3]
        pose_goal.orientation.y = pose[4]
        pose_goal.orientation.z = pose[5]
        pose_goal.orientation.w = pose[6]
        
        move_group.set_pose_target(pose_goal)
        # pose = list(np.copy(pose))

        # for i in range(3):
        #     pose[i] /= 1000.0
        print(pose)
        # move_group.set_pose_target(pose)
        move_group.set_max_velocity_scaling_factor(0.5)
        # plan = move_group.go(wait=True)
        plan2 = move_group.plan(pose_goal)
        display_trajectory = moveit_msgs.msg.DisplayTrajectory()
        display_trajectory.trajectory_start = self.robot.get_current_state()
        display_trajectory.trajectory.append(plan2)
        self.display_trajectory_publisher.publish(display_trajectory)
        value = raw_input("Replanning? (y/n)")
        while (value != 'n' ):
            plan2 = move_group.plan(pose_goal)
            display_trajectory = moveit_msgs.msg.DisplayTrajectory()
            display_trajectory.trajectory_start = self.robot.get_current_state()
            display_trajectory.trajectory.append(plan2)
            self.display_trajectory_publisher.publish(display_trajectory)
            value = raw_input("Replanning? (y/n)")
        move_group.execute(plan2,wait=True)
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

    def plan_cartesian_remove_cap(self):

        move_group = self.move_group

        # Set Max velocity of this motion
        move_group.set_max_velocity_scaling_factor(0.4)
        ##
        ## Cartesian Paths
        ## ^^^^^^^^^^^^^^^
        ## You can plan a Cartesian path directly by specifying a list of waypoints
        ## for the end-effector to go through. If executing  interactively in a
        ## Python shell, set scale = 1.0.
        ##
        waypoints = []
        wpose = move_group.get_current_pose().pose

        wpose.position.z += 0.04
        waypoints.append(copy.deepcopy(wpose))
        wpose.position.x -= 0.05
        waypoints.append(copy.deepcopy(wpose))
        wpose.position.x -= 0.05
        waypoints.append(copy.deepcopy(wpose))

        # We want the Cartesian path to be interpolated at a resolution of 1 cm
        # which is why we will specify 0.01 as the eef_step in Cartesian
        # translation.  We will disable the jump threshold by setting it to 0.0,
        # ignoring the check for infeasible jumps in joint space, which is sufficient
        # for this tutorial.
        (plan, fraction) = move_group.compute_cartesian_path(
            waypoints,   # waypoints to follow
            0.001,        # eef_step --> 1mm
            0.0)         # jump_threshold

        # Note: We are just planning, not asking move_group to actually move the robot yet:
        move_group.execute(plan, wait=True)
        return plan, fraction

    def plan_cartesian_left(self):

        move_group = self.move_group

        # Set Max velocity of this motion
        move_group.set_max_velocity_scaling_factor(0.4)
        ##
        ## Cartesian Paths
        ## ^^^^^^^^^^^^^^^
        ## You can plan a Cartesian path directly by specifying a list of waypoints
        ## for the end-effector to go through. If executing  interactively in a
        ## Python shell, set scale = 1.0.
        ##
        waypoints = []
        wpose = move_group.get_current_pose().pose

        wpose.position.x += 0.05
        waypoints.append(copy.deepcopy(wpose))
        wpose.position.x += 0.05
        waypoints.append(copy.deepcopy(wpose))
        wpose.position.x += 0.05
        waypoints.append(copy.deepcopy(wpose))
        wpose.position.x += 0.05
        waypoints.append(copy.deepcopy(wpose))

        # We want the Cartesian path to be interpolated at a resolution of 1 cm
        # which is why we will specify 0.01 as the eef_step in Cartesian
        # translation.  We will disable the jump threshold by setting it to 0.0,
        # ignoring the check for infeasible jumps in joint space, which is sufficient
        # for this tutorial.
        (plan, fraction) = move_group.compute_cartesian_path(
            waypoints,   # waypoints to follow
            0.001,        # eef_step --> 1mm
            0.0)         # jump_threshold

        # Note: We are just planning, not asking move_group to actually move the robot yet:
        move_group.execute(plan, wait=True)
        return plan, fraction

    def plan_cartesian_path(self,x=0,y=0,z=0):
        move_group = self.move_group

        # Set Max velocity of this motion
        move_group.set_max_velocity_scaling_factor(0.5)
        waypoints = []
        wpose = move_group.get_current_pose().pose

        wpose.position.x += x
        wpose.position.y += y
        wpose.position.z += z
        waypoints.append(copy.deepcopy(wpose))

        (plan, fraction) = move_group.compute_cartesian_path(waypoints,0.001,0.0)         

        display_trajectory = moveit_msgs.msg.DisplayTrajectory()
        display_trajectory.trajectory_start = self.robot.get_current_state()
        display_trajectory.trajectory.append(plan)
        self.display_trajectory_publisher.publish(display_trajectory)
        value = raw_input("Replanning? (y/n)")
        while (value != 'n' ):
            (plan, fraction) = move_group.compute_cartesian_path(
                waypoints,  # waypoints to follow
                0.001,  # eef_step --> 1mm
                0.0)  # jump_threshold
            display_trajectory = moveit_msgs.msg.DisplayTrajectory()
            display_trajectory.trajectory_start = self.robot.get_current_state()
            display_trajectory.trajectory.append(plan)
            self.display_trajectory_publisher.publish(display_trajectory)
            value = raw_input("Replanning? (y/n)")
        move_group.execute(plan,wait=True)

        return plan, fraction


    def plan_cartesian_up(self):

        move_group = self.move_group

        # Set Max velocity of this motion
        move_group.set_max_velocity_scaling_factor(0.4)
        waypoints = []
        wpose = move_group.get_current_pose().pose

        wpose.position.z += 0.04
        waypoints.append(copy.deepcopy(wpose))
        wpose.position.z += 0.04
        waypoints.append(copy.deepcopy(wpose))

        (plan, fraction) = move_group.compute_cartesian_path(
            waypoints,   # waypoints to follow
            0.001,        # eef_step --> 1mm
            0.0)         # jump_threshold

        # Note: We are just planning, not asking move_group to actually move the robot yet:
        move_group.execute(plan, wait=True)
        return plan, fraction

    def plan_cartesian_down(self):

        move_group = self.move_group

        # Set Max velocity of this motion
        move_group.set_max_velocity_scaling_factor(0.4)
        waypoints = []
        wpose = move_group.get_current_pose().pose

        wpose.position.z -= 0.04
        waypoints.append(copy.deepcopy(wpose))
        wpose.position.z -= 0.04
        waypoints.append(copy.deepcopy(wpose))

        (plan, fraction) = move_group.compute_cartesian_path(
            waypoints,   # waypoints to follow
            0.001,        # eef_step --> 1mm
            0.0)         # jump_threshold

        # Note: We are just planning, not asking move_group to actually move the robot yet:
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
        print("gripper")
        raw_input()
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
            # data = np.flip(data,0)
            path = self.rospack.get_path('move_robot')+'/src/cip_data/figure_depth0'
            np.save(path, data)
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
            # data = np.flip(data,0)
            # plt.imshow(data)
            plt.imsave(self.rospack.get_path('move_robot')+'/src/cip_data/figure_rgb0.png', data)
            self.rgb_trigger = False
        else:
            pass

    def get_tf(self):
        (trans,rot) = self.listener.lookupTransform('mani1_eff', 'dummy_link', rospy.Time(0))
        # (trans,rot) = self.listener.lookupTransform('base_footprint', 'map', rospy.Time(0))
        return (trans,rot)

    def gogogogo(self):
        move_group = self.move_group
        move_group.clear_pose_targets()
        pose_goal=move_group.get_current_pose().pose
        pose_goal.position.x =0.24642
        pose_goal.position.y =0.0013
        pose_goal.position.z =1.05078
        pose_goal.orientation.x =-0.0023
        pose_goal.orientation.y =0.8190
        pose_goal.orientation.z =0.0024
        pose_goal.orientation.w =0.5737
        pose_goal.position.x =0.244
        pose_goal.position.y =1.5
        pose_goal.position.z =1.05078
        pose_goal.orientation.x =-0.0023
        pose_goal.orientation.y =0.8190
        pose_goal.orientation.z =0.0024
        pose_goal.orientation.w =0.5737
        move_group.set_joint_value_target(pose_goal,"mani1_eff")
        plan2 = move_group.plan()
        move_group.execute(plan2, wait=True)

def save_depth(msg, path):
    width = msg.width
    height = msg.height
    data = np.fromstring(msg.data,dtype=np.uint16)
    data = np.reshape(data,(height,width))
    np.save(path, data)
    plt.imsave(path+".png", data)

def save_rgb(msg, path):
    width = msg.width
    height = msg.height
    data = np.fromstring(msg.data,dtype=np.uint8)
    data = np.reshape(data,(height,width,3))
    plt.imsave(path, data)

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
        manipulator1 = MoveGroupPythonIntefaceTutorial('manipulator1', True) #right
        manipulator2 = MoveGroupPythonIntefaceTutorial('manipulator2', False) #left

        print( "============ Press `Enter` to execute a movement using a joint state goal ...")
        manipulator = False
        if manipulator:
            # attatch_safety(manipulator1,manipulator2)

            # original z + 0.08 m
            box_site = [456.44,-506.758,422.519 + 80.0,0.70876,-0.705433,-0.00329363,-0.00356293]
            cap_site1 = [249.65,-530.613+60.0,527.901 + 80.0,0.714006,-0.700103,0.00483454,-0.00529129]
            cap_site2 = [-356.801,-542.494,482.393 + 80.0,0.714018,-0.700091,0.00476336,-0.00529695]

            ob1_site = [ 56.801,-542.494,482.393 + 80.0,0.714018,-0.700091,0.00476336,-0.00529695]

            ob2_site = [-106.801,-530,482.393 + 80.0,0.714018,-0.700091,0.00476336,-0.00529695]

            # gripper
            grasp1 = 0.015
            grasp2 = 0.035
            open = 0.07
            maxvel = 1

            print("mani1 home")
            manipulator1.go_to_home_state()

            print("mani2 home")
            manipulator2.go_to_home_state()

            print("ready")
            manipulator1.go_to_state([1.5708,0.1745,0,1.3963,0,1.5708,0])

            box_pose = geometry_msgs.msg.PoseStamped()

#             # box
#             box_pose.header.frame_id = "mani1_eff"
#             box_pose.pose.orientation.w = 1.0
#             box_pose.pose.position.z = 0.2
#             box_pose.pose.position.y = 0
#             box_pose.pose.position.x = 0
#             box_name = "box"
#             manipulator1.scene.add_box("box", box_pose, size=(0.1, 0.1, 0.1))
#             manipulator1.scene.attach_box("mani1_eff","box",touch_links = ["mani1_eff"])

            print("put box")
            manipulator1.set_pose_goal(box_site)
            print("go down")
            manipulator1.plan_cartesian_path(x=0,y=0,z=-0.08)
#            manipulator1.plan_cartesian_down()

            # manipulator1.scene.remove_attached_object("mani1_eff","box")
            # manipulator1.scene.remove_world_object("box")
            # manipulator2.scene.remove_world_object("box")
            print("go to..")
            manipulator2.set_pose_goal(cap_site2)
            print("grab cap handle")
            manipulator2.set_pose_goal(cap_site1)
            print("go down")
            manipulator2.plan_cartesian_path(x=0,y=0,z=-0.08)
#            manipulator2.plan_cartesian_down()

            manipulator2.gripper_request(grasp2)

            print("remove cap")
            manipulator2.plan_cartesian_path(x=0,y=0,z=0.04)
            print("go side")
            manipulator2.plan_cartesian_path(x=-0.3,y=0,z=0)
#            manipulator2.plan_cartesian_remove_cap()

            # manipulator2.plan_cartesian_path(x=-0.08, y=0, z=0)
            print("go to put the cap")
            manipulator2.set_pose_goal(cap_site2)
            print("go down")
            manipulator2.plan_cartesian_path(x=0,y=0,z=-0.08)
#            manipulator2.plan_cartesian_down()

            manipulator2.gripper_request(open)

            ##### if use mani2 to grab ob1
            print("go up")
            manipulator2.plan_cartesian_path(x=0,y=0,z=0.08,)
#            manipulator2.plan_cartesian_up()

            print("go to grab object")
            manipulator2.set_pose_goal(ob1_site)

            print("go down")
            manipulator2.plan_cartesian_path(x=0,y=0,z=-0.08)
#            manipulator2.plan_cartesian_down()

            manipulator2.gripper_request(grasp2) # ob1

            print("go up")
            manipulator2.plan_cartesian_path(x=0,y=0,z=0.08)
#            manipulator2.plan_cartesian_up()

            print("go to put object")
            manipulator2.set_pose_goal(cap_site1)

            manipulator2.gripper_request(open)

            print("go to grab object2")
            manipulator2.set_pose_goal(ob2_site)

            print("go down")
            manipulator2.plan_cartesian_path(x=0,y=0,z=-0.08)
            #manipulator2.plan_cartesian_down()

            manipulator2.gripper_request(grasp2)  # ob2

            print("go up")
            manipulator2.plan_cartesian_path(x=0,y=0,z=0.08)
#            manipulator2.plan_cartesian_up()

            print("go to put object2")
            manipulator2.set_pose_goal(cap_site1)

            manipulator2.gripper_request(open)

            ########## if close box
            print("go side")
            manipulator2.plan_cartesian_path(x=-0.08, y=0, z=0)
            print("go to bring the cap")
            manipulator2.set_pose_goal(cap_site2)
            print("go down")
            manipulator2.plan_cartesian_path(x=0,y=0,z=-0.08)
#            manipulator2.plan_cartesian_down()

            manipulator2.gripper_request(grasp2)

            print("go up")
            manipulator2.plan_cartesian_path(x=0,y=0,z=0.08)
#            manipulator2.plan_cartesian_up()
            print("go side")
            manipulator2.plan_cartesian_path(x=0.08, y=0, z=0)

            print("go to cover box")
            manipulator2.set_pose_goal(cap_site1)

            print("go down")
            manipulator2.plan_cartesian_path(x=0,y=0,z=-0.08)
#            manipulator2.plan_cartesian_down()
            manipulator2.gripper_request(open)

            print("go up")
            manipulator2.plan_cartesian_path(x=0,y=0,z=0.08)
#            manipulator2.plan_cartesian_up()
            print("go side")
            manipulator2.plan_cartesian_path(x=-0.3,y=0,z=0)
            print("mani2 go home")
            manipulator2.go_to_home_state()
            manipulator1.gripper_request(open)
            print("go side")
            manipulator1.plan_cartesian_path(x=0,y=0,z=0.2)
            print("mani1 go home")
            manipulator1.go_to_home_state()


            print("done")
        else:
            rel_dist = [-4.0, -730.0, 422.519 + 65.0]

            rgb_path = manipulator1.rospack.get_path('move_robot')+'/src/cip_data/figure_rgb0.png'
            depth_path = manipulator1.rospack.get_path('move_robot')+'/src/cip_data/figure_depth0.npy'
            # txt_path = manipulator1.rospack.get_path('move_robot')+'/src/cip_data/grasping_result0.txt'
            # image_path = manipulator1.rospack.get_path('move_robot')+'/src/cip_data/grasping_result0.jpg'
            result_path = manipulator1.rospack.get_path('move_robot')+'/src/cip_data/results'
            # original z + 0.08 m
            box_site = [456.44,-506.758,422.519 + 110.0,0.70876,-0.705433,-0.00329363,-0.00356293]
            cap_site1 = [249.65,-530.613,527.901 + 80.0,0.714006,-0.700103,0.00483454,-0.00529129]
            cap_site2 = [-356.801,-542.494,482.393 + 80.0,0.714018,-0.700091,0.00476336,-0.00529695]

            put_site = [209.65,-530.613,527.901 + 80.0,0.714006,-0.700103,0.00483454,-0.00529129]
            cap_site3 = [-366.801,-542.494,482.393 + 80.0,0.714018,-0.700091,0.00476336,-0.00529695]
            cap_site4 = [252.65, -535.613, 527.901 + 80.0, 0.714006, -0.700103, 0.00483454, -0.00529129]

            # gripper
            grasp1 = 0.025
            grasp2 = 0.04
            spaner = 0.01
            driver = 0.035
            open = 0.07
            maxvel = 1


#            rgb_msg = rospy.wait_for_message("/camera2/color/image_raw", Image)
#            depth_msg = rospy.wait_for_message("/camera2/depth/image_rect_raw", Image)
#            save_rgb(rgb_msg, rgb_path)
#            save_depth(depth_msg, depth_path)

            print("wait for object detecting")

            #crop_and_resize(rgb_path, depth_path)
#            grasping_point = calc_grasping_point(rgb_path, depth_path, result_path)
#            print(grasping_point)

#            center = grasping_point['center']
#            angle = grasping_point['angle']

            # real_position = np.array([(center[0]-320)/100*95, -(center[1]-240)/100*95, 10]) #(x,y) (mm)
            # real_position = np.array([(center[0]-320)/26.6*25, -(center[1]-240)/26.6*25, 10]) #(x,y) (mm)
#            real_position = np.array([-(center[0] - 320) / (75 * 0.74) * 50, (center[1] - 240) / (75 * 0.67) * 50,
#                                      0])  # (x,y) (mm)  /(pixel*resizing factor)*mm

#            print(real_position)
            # real_position = [0,0,0]
            # angle = 0
            # ??
            # if angle < 0:
            #     angle += pi
            # angle = np.arctan2(np.sin(angle), np.cos(angle))
            # print(angle*180/np.pi)
#            rot = R.from_euler('xyz', [180, 0, -angle * 180 / np.pi], degrees=True)
#            print(rot)
#            r_quat = rot.as_quat()

#            ob1_site = [rel_dist[0] + real_position[0], rel_dist[1] + real_position[1], rel_dist[2], r_quat[0],
#                        r_quat[1], r_quat[2], r_quat[3]]
 #           print(ob1_site)

#            ob1_site = [-109.40540540540539, -592.6865671641791, 487.519, 0.8687755510686266, -0.49520606000472595, -3.0322625815157985e-17, 5.319715988968357e-17]
            print("mani1 home")
            manipulator1.go_to_home_state()
            manipulator1.gripper_request(open)

            print("mani2 home")
            manipulator2.go_to_home_state()
            manipulator2.gripper_request(open)

            print("ready")
            manipulator1.go_to_state([1.5708, 0.1745, 0, 1.3963, 0, 1.5708, 0])
            manipulator1.gripper_request(0.04)
            manipulator1.gripper_request(grasp1)

            #
            print("put box")
            manipulator1.set_pose_goal(box_site)
            print("go down")
            manipulator1.plan_cartesian_path(x=0,y=0,z=-0.08)

            print("go to..")
            manipulator2.set_pose_goal(cap_site2)
            print("grab cap handle")
            manipulator2.set_pose_goal(cap_site1)
            print("go down")
            manipulator2.plan_cartesian_path(x=0,y=0,z=-0.1)
            manipulator2.gripper_request(grasp2)

            print("remove cap")
            manipulator2.plan_cartesian_path(x=0,y=0,z=0.06)
            print("go side")
            manipulator2.plan_cartesian_path(x=-0.08, y=0, z=0)
            print("more up")
            manipulator2.plan_cartesian_path(x=0, y=0, z=0.04)

            print("go to put the cap")
            manipulator2.set_pose_goal(cap_site2)
            print("go down")
            manipulator2.plan_cartesian_path(x=0,y=0,z=-0.08)

            manipulator2.gripper_request(open)

            print("go up")
            manipulator2.plan_cartesian_path(x=0,y=0,z=0.08,)

            print("go to grab object")
            manipulator2.set_pose_goal(ob1_site)

            print("go down")
            manipulator2.plan_cartesian_path(x=0,y=0,z=-0.07)

            # manipulator2.gripper_request(driver) # ob1
            manipulator2.gripper_request(spaner) # ob2

            print("go up")
            manipulator2.plan_cartesian_path(x=0,y=0,z=0.08)

            print("go to put object")
            manipulator2.set_pose_goal(cap_site1)
            # manipulator2.set_pose_goal(put_site)

            manipulator2.gripper_request(open)


            ########## if close box
            print("go side")
            manipulator2.plan_cartesian_path(x=-0.08, y=0, z=0)
            print("go to bring the cap")
            manipulator2.set_pose_goal(cap_site3)
            print("go down")
            manipulator2.plan_cartesian_path(x=0,y=0,z=-0.08)

            manipulator2.gripper_request(grasp2)

            print("go up")
            manipulator2.plan_cartesian_path(x=0,y=0,z=0.08)

            print("go side")
            manipulator2.plan_cartesian_path(x=0.08, y=0, z=0)

            print("go to cover box")
            manipulator2.set_pose_goal(cap_site4)

            print("go down")
            manipulator2.plan_cartesian_path(x=0,y=0,z=-0.06)

            manipulator2.gripper_request(open)

            print("go up")
            manipulator2.plan_cartesian_path(x=0,y=0,z=0.08)

            print("go side")
            manipulator2.plan_cartesian_path(x=-0.3,y=0,z=0)

            print("mani2 go home")
            manipulator2.go_to_home_state()
            #manipulator1.gripper_request(open)
            print("go up")
            #manipulator1.plan_cartesian_path(x=0,y=0,z=0.2)
            manipulator1.go_to_state([1.5708,0.1745,0,1.3963,0,1.5708,0])
            # print("mani1 go home")
            # manipulator1.go_to_home_state()




            print("done")

        print( "============ Python tutorial demo complete!")
    except rospy.ROSInterruptException:
        return
    except KeyboardInterrupt:
        return

if __name__ == '__main__':
    main()
