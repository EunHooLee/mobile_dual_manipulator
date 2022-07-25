#!/usr/bin/env python
# Software License Agreement (BSD License)
#
# Copyright (c) 2008, Willow Garage, Inc.
# All rights reserved.
#
# Redistribution and use in source and binary forms, with or without
# modification, are permitted provided that the following conditions
# are met:
#
#  * Redistributions of source code must retain the above copyright
#    notice, this list of conditions and the following disclaimer.
#  * Redistributions in binary form must reproduce the above
#    copyright notice, this list of conditions and the following
#    disclaimer in the documentation and/or other materials provided
#    with the distribution.
#  * Neither the name of Willow Garage, Inc. nor the names of its
#    contributors may be used to endorse or promote products derived
#    from this software without specific prior written permission.
#
# THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS
# "AS IS" AND ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT
# LIMITED TO, THE IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS
# FOR A PARTICULAR PURPOSE ARE DISCLAIMED. IN NO EVENT SHALL THE
# COPYRIGHT OWNER OR CONTRIBUTORS BE LIABLE FOR ANY DIRECT, INDIRECT,
# INCIDENTAL, SPECIAL, EXEMPLARY, OR CONSEQUENTIAL DAMAGES (INCLUDING,
# BUT NOT LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS OR SERVICES;
# LOSS OF USE, DATA, OR PROFITS; OR BUSINESS INTERRUPTION) HOWEVER
# CAUSED AND ON ANY THEORY OF LIABILITY, WHETHER IN CONTRACT, STRICT
# LIABILITY, OR TORT (INCLUDING NEGLIGENCE OR OTHERWISE) ARISING IN
# ANY WAY OUT OF THE USE OF THIS SOFTWARE, EVEN IF ADVISED OF THE
# POSSIBILITY OF SUCH DAMAGE.
#
# Revision $Id$

## Simple talker demo that published std_msgs/Strings messages
## to the 'chatter' topic

import os
import rospy
import math

from dxl_gripper.srv import GripperDist,GripperDistResponse

if os.name == 'nt':
    import msvcrt
    def getch():
        return msvcrt.getch().decode()
else:
    import sys, tty, termios
    fd = sys.stdin.fileno()
    old_settings = termios.tcgetattr(fd)
    def getch():
        try:
            tty.setraw(sys.stdin.fileno())
            ch = sys.stdin.read(1)
        finally:
            termios.tcsetattr(fd, termios.TCSADRAIN, old_settings)
        return ch

from dynamixel_sdk import *
#from msgpkg.msg import finger
M_PI = 3.14159265358979323846
mag_en = 0.0
t_pre = 0.0
hz = 1./100
dxl_present_position=0

k_sc = 0.55
l_length = 0.068
# Control table address
ADDR_PRO_BAUD_RATE	    = 8
ADDR_PRO_RETURN_TIME	    = 9
ADDR_PRO_OPERATING_MODE	    = 11
ADDR_PRO_HOMING_OFFSET 	    = 20
ADDR_PRO_MAX_POS 	    = 48
ADDR_PRO_MIN_POS 	    = 52
ADDR_PRO_TORQUE_ENABLE      = 64               # Control table address is different in Dynamixel model
ADDR_PRO_PROFILE_VELOCITY   = 112
ADDR_PRO_GOAL_POSITION      = 116
ADDR_PRO_PRESENT_POSITION   = 132

# Data Byte Length
LEN_PRO_GOAL_POSITION       = 4
LEN_PRO_PRESENT_POSITION    = 4
LEN_PRO_PROFILE_VELOCITY    = 4


# Protocol version
PROTOCOL_VERSION            = 2.0               # See which protocol version is used in the Dynamixel

# Default setting
DXL1_ID                      = 1               # Dynamixel#1 ID : 1
DXL2_ID                      = 2               # Dynamixel#2 ID : 2
BAUDRATE                    = 1000000             # Dynamixel default baudrate : 57600
DEVICENAME                  = '/dev/ttyUSB0'    # Check which port is being used on your controller
                                                # ex) Windows: "COM1"   Linux: "/dev/ttyUSB0" Mac: "/dev/tty.usbserial-*"
BAUD_RATE_SET		    	= 3			# 1000000
OPERATING_MODE		    	= 5   # Current-based Position Control Mode
#Max Position Limit(48) and Min Position Limit(52) are only used in Position Control Mode with a single turn.

# ** setserial /dev/ttyUSB0 low_latency - if you want more communication speed, write this in terminal   https://github.com/ROBOTIS-GIT/DynamixelSDK/issues/80


TORQUE_ENABLE               = 1                 # Value for enabling the torque
TORQUE_DISABLE              = 0                 # Value for disabling the torque

DXL_MOVING_STATUS_THRESHOLD = 20                # Dynamixel moving status threshold


portHandler = PortHandler(DEVICENAME)
packetHandler = PacketHandler(PROTOCOL_VERSION)

groupSyncWrite = GroupSyncWrite(portHandler, packetHandler, ADDR_PRO_GOAL_POSITION, LEN_PRO_GOAL_POSITION)
groupSyncRead = GroupSyncRead(portHandler, packetHandler, ADDR_PRO_PRESENT_POSITION, LEN_PRO_PRESENT_POSITION)


if portHandler.openPort():
    print("Succeeded to open the port")
else:
    print("Failed to open the port")
    print("Press any key to terminate...")
    getch()
    quit()


if portHandler.setBaudRate(BAUDRATE):
    print("Succeeded to change the baudrate")
else:
    print("Failed to change the baudrate")
    print("Press any key to terminate...")
    getch()
    quit()


dxl_comm_result, dxl_error = packetHandler.write1ByteTxRx(portHandler, DXL1_ID, ADDR_PRO_TORQUE_ENABLE, TORQUE_ENABLE)
if dxl_comm_result != COMM_SUCCESS:
    print("%s" % packetHandler.getTxRxResult(dxl_comm_result))
elif dxl_error != 0:
    print("%s" % packetHandler.getRxPacketError(dxl_error))
else:
    print("Dynamixel#%d has been successfully connected" % DXL1_ID)


dxl_comm_result, dxl_error = packetHandler.write1ByteTxRx(portHandler, DXL2_ID, ADDR_PRO_TORQUE_ENABLE, TORQUE_ENABLE)
if dxl_comm_result != COMM_SUCCESS:
    print("%s" % packetHandler.getTxRxResult(dxl_comm_result))
elif dxl_error != 0:
    print("%s" % packetHandler.getRxPacketError(dxl_error))
else:
    print("Dynamixel#%d has been successfully connected" % DXL2_ID)


dxl_addparam_result = groupSyncRead.addParam(DXL1_ID)
if dxl_addparam_result != True:
    print("[ID:%03d] groupSyncRead addparam failed" % DXL1_ID)
    quit()


dxl_addparam_result = groupSyncRead.addParam(DXL2_ID)
if dxl_addparam_result != True:
    print("[ID:%03d] groupSyncRead addparam failed" % DXL2_ID)
    quit()

	
def dis2inc(dist):
	if dist > 0.1:
		dist = 0.1
	elif dist < 0:
		dist = 0
	
	dist = dist/2 + 0.0065  # 0.0065 --> adjust using silicon thickness
	inc = int(math.degrees(math.asin((dist-0.0175)/0.07))/0.0879)
	
	return inc

def gripper_sync_move(req):
	global param_goal_pos
	
	complete = 0	
	
	param_goal_pos = dis2inc(req.dist)
	
	dxl_goal_pos1 = 2048 - param_goal_pos
	dxl_goal_pos2 = 2048 + param_goal_pos

	param_goal_pos1 = [DXL_LOBYTE(DXL_LOWORD(dxl_goal_pos1)), DXL_HIBYTE(DXL_LOWORD(dxl_goal_pos1)), DXL_LOBYTE(DXL_HIWORD(dxl_goal_pos1)), DXL_HIBYTE(DXL_HIWORD(dxl_goal_pos1))]

	param_goal_pos2 = [DXL_LOBYTE(DXL_LOWORD(dxl_goal_pos2)), DXL_HIBYTE(DXL_LOWORD(dxl_goal_pos2)), DXL_LOBYTE(DXL_HIWORD(dxl_goal_pos2)), DXL_HIBYTE(DXL_HIWORD(dxl_goal_pos2))]

	dxl_addparam_result = groupSyncWrite.addParam(DXL1_ID, param_goal_pos1)
	if dxl_addparam_result != True:
	    print("[ID:%03d] groupSyncWrite addparam failed" % DXL1_ID)
	    quit()
	dxl_addparam_result = groupSyncWrite.addParam(DXL2_ID, param_goal_pos2)
	if dxl_addparam_result != True:
	    print("[ID:%03d] groupSyncWrite addparam failed" % DXL2_ID)
	    quit()

	
	dxl_comm_result = groupSyncWrite.txPacket()
	if dxl_comm_result != COMM_SUCCESS:
	    print("%s" % packetHandler.getTxRxResult(dxl_comm_result))

	groupSyncWrite.clearParam()

	while 1:
	   
	    dxl_comm_result = groupSyncRead.txRxPacket()
	    if dxl_comm_result != COMM_SUCCESS:
	        print("%s" % packetHandler.getTxRxResult(dxl_comm_result))

	    dxl_getdata_result = groupSyncRead.isAvailable(DXL1_ID, ADDR_PRO_PRESENT_POSITION, LEN_PRO_PRESENT_POSITION)
	    if dxl_getdata_result != True:
	        print("[ID:%03d] groupSyncRead getdata failed" % DXL1_ID)
	        quit()
	    dxl_getdata_result = groupSyncRead.isAvailable(DXL2_ID, ADDR_PRO_PRESENT_POSITION, LEN_PRO_PRESENT_POSITION)
	    if dxl_getdata_result != True:
	        print("[ID:%03d] groupSyncRead getdata failed" % DXL2_ID)
	        quit()

	    dxl1_present_pos = groupSyncRead.getData(DXL1_ID, ADDR_PRO_PRESENT_POSITION, LEN_PRO_PRESENT_POSITION)
	    dxl2_present_pos = groupSyncRead.getData(DXL2_ID, ADDR_PRO_PRESENT_POSITION, LEN_PRO_PRESENT_POSITION)
	    
	    print("[ID:%03d] GoalPos:%03d  PresPos:%03d\t[ID:%03d] GoalPos:%03d  PresPos:%03d" % (DXL1_ID, dxl_goal_pos1, dxl1_present_pos, DXL2_ID, dxl_goal_pos2, dxl2_present_pos))
	    
	    if not ((abs(dxl_goal_pos1 - dxl1_present_pos) > DXL_MOVING_STATUS_THRESHOLD) and (abs(dxl_goal_pos2 - dxl2_present_pos) > DXL_MOVING_STATUS_THRESHOLD)):
	    	complete = 1
	        break


	return GripperDistResponse(complete)



def gripper_node():
	global param_goal_pos

	param_goal_pos = 200
	
	dxl_goal_pos1 = 2048 - param_goal_pos
	dxl_goal_pos2 = 2048 + param_goal_pos

	param_goal_pos1 = [DXL_LOBYTE(DXL_LOWORD(dxl_goal_pos1)), DXL_HIBYTE(DXL_LOWORD(dxl_goal_pos1)), DXL_LOBYTE(DXL_HIWORD(dxl_goal_pos1)), DXL_HIBYTE(DXL_HIWORD(dxl_goal_pos1))]

	param_goal_pos2 = [DXL_LOBYTE(DXL_LOWORD(dxl_goal_pos2)), DXL_HIBYTE(DXL_LOWORD(dxl_goal_pos2)), DXL_LOBYTE(DXL_HIWORD(dxl_goal_pos2)), DXL_HIBYTE(DXL_HIWORD(dxl_goal_pos2))]

	dxl_addparam_result = groupSyncWrite.addParam(DXL1_ID, param_goal_pos1)
	if dxl_addparam_result != True:
	    print("[ID:%03d] groupSyncWrite addparam failed" % DXL1_ID)
	    quit()


	dxl_addparam_result = groupSyncWrite.addParam(DXL2_ID, param_goal_pos2)
	if dxl_addparam_result != True:
	    print("[ID:%03d] groupSyncWrite addparam failed" % DXL2_ID)
	    quit()

	dxl_comm_result = groupSyncWrite.txPacket()
	if dxl_comm_result != COMM_SUCCESS:
	    print("%s" % packetHandler.getTxRxResult(dxl_comm_result))

	groupSyncWrite.clearParam()
	
	
	rospy.init_node('gripper_1')
	s = rospy.Service('gripper_dist_1', GripperDist, gripper_sync_move)
	
	rospy.spin()

if __name__ == '__main__':
    try:
        t_pre = time.time()
        gripper_node()
    except rospy.ROSInterruptException:
    	# Disable Dynamixel#1 Torque
	dxl_comm_result, dxl_error = packetHandler.write1ByteTxRx(portHandler, DXL1_ID, ADDR_PRO_TORQUE_ENABLE, TORQUE_DISABLE)
	if dxl_comm_result != COMM_SUCCESS:
			print("%s" % packetHandler.getTxRxResult(dxl_comm_result))
	elif dxl_error != 0:
			print("%s" % packetHandler.getRxPacketError(dxl_error))

	# Disable Dynamixel#2 Torque
	dxl_comm_result, dxl_error = packetHandler.write1ByteTxRx(portHandler, DXL2_ID, ADDR_PRO_TORQUE_ENABLE, TORQUE_DISABLE)
	if dxl_comm_result != COMM_SUCCESS:
			print("%s" % packetHandler.getTxRxResult(dxl_comm_result))
	elif dxl_error != 0:
			print("%s" % packetHandler.getRxPacketError(dxl_error))

	# Close port
	portHandler.closePort()
    
        pass
