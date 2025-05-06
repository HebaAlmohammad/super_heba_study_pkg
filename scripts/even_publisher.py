#!/usr/bin/env python3
import rospy
from std_msgs.msg import Int32, String

rospy.init_node('even_numbers_publisher')
pub = rospy.Publisher('even_numbers', Int32, queue_size=10)
overflow_pub = rospy.Publisher('overflow_topic', String, queue_size=10)
rate = rospy.Rate(10)  # 10 Hz

counter = 0

while not rospy.is_shutdown():
    if counter <= 100:
        pub.publish(counter)
        counter += 2
    else:
        overflow_pub.publish("Counter reached 100!")
        counter = 0
    rate.sleep()
