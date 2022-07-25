#!/usr/bin/env python


import sys
import rospy
## END_SUB_TUTORIAL
from mservo_msg.msg import traj_1d

def commander():
    pub = rospy.Publisher('arm1',traj_1d,queue_size=10)
    rospy.init_node('commander', anonymous=True)

    joint_value = {
        'home' : [0,0,0,0,0,0,0],
        'state1' : [0,-90,0,0,0,0,0],
        'state2' : [0,-90,0,90,0,0,0],
        'state3' : [0,-90,-90,90,0,0,0],
        'state4' : [0,-90,0,0,0,90,0],
        'state5' : [0,-90,0,0,90,90,0],
        # 'state6' : [0,-90,0,0,90,90,0],
        # 'pose1' : [-60,-65,15,95,5,70,0],
        # 'pose2' : [10,-50,50,70,50,30,0],
        # 'pose3' : [90,30,80,-70,-40,-20,0],
        # 'pose4' : [20,-50,90,-80,-40,30,0],
        'pose0' : [-12,-36,0,-92,115,-65,0],  # no load
        'pose0w' : [-6.15,-32,0,-92,110,-65,0],  # with load
        'pose1' : [22,-76,20,54,15,-65,0],
        'pose2' : [-10,95,-38,-64,55,54,0],
        'pose3' : [45,15,58,110,0,-54,0],

        'test1' : [0,0,0,0,0,90,0],
        'test2' : [0,0,0,-90,0,0,0],
        'test3' : [0,-90,0,0,0,0,0],
        'test4' : [0,-90,0,90,0,0,0]
    }
    # 'pose1' : [-80,50,75,95,-50,85,30],
    # 'pose2' : [10,-50,85,70,50,-80,-10],
    # 'pose3' : [90,30,80,-90,-80,90,40],
    # 'pose4' : [20,-50,90,-80,-40,30,-25]
    print "Press Enter to go home position"
    raw_input()
    command = joint_value['home']
    pub.publish(command)

    while not rospy.is_shutdown():
        value = raw_input("Command (joint/pose_n/pose_w) : ")
        if (value=='joint'):
            print "Press Enter to go each position"
            raw_input()
            command = joint_value['state1']
            print "Joint value = ", command
            pub.publish(command)
            raw_input()
            command = joint_value['state2']
            print "Joint value = ", command
            pub.publish(command)
            raw_input()
            command = joint_value['state3']
            print "Joint value = ", command
            pub.publish(command)
            raw_input()
            command = joint_value['state2']
            print "Joint value = ", command
            pub.publish(command)
            raw_input()
            command = joint_value['state1']
            print "Joint value = ", command
            pub.publish(command)
            raw_input()
            command = joint_value['state4']
            print "Joint value = ", command
            pub.publish(command)
            raw_input()
            command = joint_value['state5']
            print "Joint value = ", command
            pub.publish(command)
            raw_input()
            command = joint_value['state4']
            print "Joint value = ", command
            pub.publish(command)
            # raw_input()
            # command = joint_value['state2']
            # print "Joint value = ", command
            # pub.publish(command)
            raw_input()
            command = joint_value['state1']
            print "Joint value = ", command
            pub.publish(command)
            raw_input()
            command = joint_value['home']
            print "Joint value = ", command
            pub.publish(command)
        elif (value=='pose_n'):
            print "Press Enter to go each position"
            raw_input()
            command = joint_value['pose0']
            print "#1 Joint value = ", command
            pub.publish(command)
            raw_input()
            command = joint_value['pose1']
            print "#2 Joint value = ", command
            pub.publish(command)
            raw_input()
            command = joint_value['pose2']
            print "#3 Joint value = ", command
            pub.publish(command)
            raw_input()
            command = joint_value['pose3']
            print "#4 Joint value = ", command
            pub.publish(command)
            raw_input()
            command = joint_value['pose0']
            print "#1 Joint value = ", command
            pub.publish(command)
            raw_input()
            command = joint_value['home']
            print "Joint value = ", command
            pub.publish(command)
        elif (value=='pose_w'):
            print "Press Enter to go each position"
            raw_input()
            command = joint_value['pose0w']
            print "#1 Joint value = ", command
            pub.publish(command)
            raw_input()
            command = joint_value['pose1']
            print "#2 Joint value = ", command
            pub.publish(command)
            raw_input()
            command = joint_value['pose2']
            print "#3 Joint value = ", command
            pub.publish(command)
            raw_input()
            command = joint_value['pose3']
            print "#4 Joint value = ", command
            pub.publish(command)
            raw_input()
            command = joint_value['pose0w']
            print "#1 Joint value = ", command
            pub.publish(command)
            raw_input()
            command = joint_value['home']
            print "Joint value = ", command
            pub.publish(command)
        elif (value=='test'):
            print "Press Enter to go each position"
            raw_input()
            command = joint_value['test1']
            print "#1 Joint value = ", command
            pub.publish(command)
            raw_input()
            command = joint_value['test2']
            print "#2 Joint value = ", command
            pub.publish(command)
            raw_input()
            command = joint_value['test3']
            print "#3 Joint value = ", command
            pub.publish(command)
            raw_input()
            command = joint_value['test4']
            print "#4 Joint value = ", command
            pub.publish(command)
            raw_input()
            command = joint_value['home']
            print "Joint value = ", command
            pub.publish(command)


def main():
    try:
        commander()
    except rospy.ROSInterruptException:
        print "============ Payload test complete!"
        return
    except KeyboardInterrupt:
        print "============ Payload test complete!"
        return

if __name__ == '__main__':
    main()
