#!/usr/bin/env python3
import rospy
from std_msgs.msg import Int32

def callback(msg):
    rospy.loginfo("Received even number: %d", msg.data)

rospy.init_node('even_numbers_listener')
rospy.Subscriber('even_numbers', Int32, callback)
rospy.spin()
