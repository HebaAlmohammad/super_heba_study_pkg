#!/usr/bin/env python3
import rospy
from std_msgs.msg import String

rospy.init_node('sender')
pub = rospy.Publisher('chatter', String, queue_size=10)
rate = rospy.Rate(10)  # 10Hz

while not rospy.is_shutdown():
    msg = "Hello world %s" % rospy.get_time()
    pub.publish(msg)
    rate.sleep()
