#!/usr/bin/env python


import sys
import copy
import rospy
import moveit_commander
import moveit_msgs.msg
import geometry_msgs.msg
from math import pi
from std_msgs.msg import String
from moveit_commander.conversions import pose_to_list
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
  def __init__(self):
    super(MoveGroupPythonIntefaceTutorial, self).__init__()

    ## BEGIN_SUB_TUTORIAL setup
    ##
    ## First initialize `moveit_commander`_ and a `rospy`_ node:
    moveit_commander.roscpp_initialize(sys.argv)
    rospy.init_node('move_group_python_interface_tutorial', anonymous=True)

    ## Instantiate a `RobotCommander`_ object. Provides information such as the robot's
    ## kinematic model and the robot's current joint states
    robot = moveit_commander.RobotCommander()

    ## Instantiate a `PlanningSceneInterface`_ object.  This provides a remote interface
    ## for getting, setting, and updating the robot's internal understanding of the
    ## surrounding world:
    scene = moveit_commander.PlanningSceneInterface()


    ## Instantiate a `MoveGroupCommander`_ object.  This object is an interface
    ## to a planning group (group of joints).  In this tutorial the group is the primary
    ## arm joints in the Panda robot, so we set the group's name to "panda_arm".
    ## If you are using a different robot, change this value to the name of your robot
    ## arm planning group.
    ## This interface can be used to plan and execute motions:

    ################ NOT ROBOT's NAME --> ARM's NAME IN MoveIt  ######################
    ################ I set up this name in MoveIt Setup Assistant ####################
    ################ Not sure but I might modify this name in SRDF files  ############
    group_name = "arm_ver1"
    move_group = moveit_commander.MoveGroupCommander(group_name)


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
    print "============ Available Planning Groups:", robot.get_group_names()

    # Sometimes for debugging it is useful to print the entire state of the
    # robot:
    print "============ Printing robot state"
    print robot.get_current_state()
    print ""
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



  def go_to_joint_state1(self):

    move_group = self.move_group


    # left middle side
    joint_goal = move_group.get_current_joint_values()
    joint_goal[0] = -pi / 2
    joint_goal[1] = pi / 4
    joint_goal[2] = -pi / 4
    joint_goal[3] = 0
    joint_goal[4] = -pi / 4
    joint_goal[5] = pi / 2
    joint_goal[6] = -pi / 2
    move_group.set_max_velocity_scaling_factor(0.4)

    move_group.go(joint_goal, wait=True)

    # Calling ``stop()`` ensures that there is no residual movement
    move_group.stop()

    ## END_SUB_TUTORIAL

    # For testing:
    current_joints = move_group.get_current_joint_values()
    return all_close(joint_goal, current_joints, 0.01)

  def go_to_joint_state2(self):
    move_group = self.move_group

    # right middle side
    joint_goal = move_group.get_current_joint_values()
    joint_goal[0] = -pi / 2
    joint_goal[1] = -pi / 4
    joint_goal[2] = pi / 4
    joint_goal[3] = 0
    joint_goal[4] = pi / 4
    joint_goal[5] = -pi / 2
    joint_goal[6] = pi / 2


    move_group.set_max_velocity_scaling_factor(0.4)
    move_group.go(joint_goal, wait=True)

    # Calling ``stop()`` ensures that there is no residual movement
    move_group.stop()

    ## END_SUB_TUTORIAL

    # For testing:
    current_joints = move_group.get_current_joint_values()
    return all_close(joint_goal, current_joints, 0.01)

  def go_to_joint_state3(self):
    move_group = self.move_group

    # right down side
    joint_goal = move_group.get_current_joint_values()
    joint_goal[0] = - pi / 4
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



  def go_to_pose_goal1(self):
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
    pose_goal.orientation.w = 1.0

    pose_goal.position.x = 0.4
    pose_goal.position.y = 0.0
    pose_goal.position.z = 0.3

    # move_group.set_pose_target(pose_goal)
    move_group.set_pose_target([0.0, 0.6, 0.5, -pi/2, 0, 0])
  # move_group.set_rpy_target([pi, 0, pi/2])

    ## Now, we call the planner to compute the plan and execute it.
    # plan3 = move_group.plan()
    #
    # rospy.sleep(3)
    move_group.set_max_velocity_scaling_factor(0.2)

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
    return all_close(pose_goal, current_pose, 0.01)



  def plan_cartesian_path(self, scale=1):

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

    wpose.position.y += scale * 0.07  # Second move forward/backwards in (x)
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


    ## END_SUB_TUTORIAL


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


def main():
  try:
    print ""
    print "----------------------------------------------------------"
    print "Welcome to the MoveIt! MoveGroup Python Interface Tutorial"
    print "----------------------------------------------------------"
    print "Press Ctrl-D to exit at any time"
    print ""
    print "============ Press `Enter` to begin the tutorial by setting up the moveit_commander ..."
    # raw_input()
    tutorial = MoveGroupPythonIntefaceTutorial()

    print "============ Press `Enter` to execute a movement using a joint state goal ..."
    # raw_input()
    # tutorial.go_to_joint_state1()

    # raw_input()
    # tutorial.go_to_joint_state3()

    # raw_input()
    # tutorial.go_to_joint_state3()
    #
    raw_input()
    tutorial.go_to_pose_goal1()


    # print "============ Press `Enter` to execute a movement using a pose goal ..."
    # raw_input()

    # move_group.setMaxVelocityScalingFactor(0.2);
    #
    # joint_goa2 = move_group.get_current_joint_values()
    # def moveit_commander.move_group.MoveGroupCommander.set_max_velocity_scaling_factor
    # max_velocity_scaling_factor = 0.14

    # print "============ Press `Enter` to plan and display a Cartesian path ..."
    # raw_input()
    # cartesian_plan, fraction = tutorial.plan_cartesian_path()


    # print "============ Press `Enter` to plan and display a Cartesian path ..."
    # raw_input()
    # cartesian_plan, fraction = tutorial.plan_cartesian_path_out()
    # print "============ Press `Enter` to display a saved trajectory (this will replay the Cartesian path)  ..."
    # raw_input()
    # tutorial.display_trajectory(cartesian_plan)

    # print "============ Press `Enter` to execute a saved path ..."
    # raw_input()
    # tutorial.execute_plan(cartesian_plan)

    raw_input()
    tutorial.go_to_home_state()


    print "============ Python tutorial demo complete!"
  except rospy.ROSInterruptException:
    return
  except KeyboardInterrupt:
    return

if __name__ == '__main__':
  main()
