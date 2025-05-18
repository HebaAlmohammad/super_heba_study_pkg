#!/usr/bin/env python
import rospy
from geometry_msgs.msg import Twist

def follow():
    rospy.init_node('turtle_follower')
    pub = rospy.Publisher('/turtle2/cmd_vel', Twist, queue_size=10)
    rate = rospy.Rate(10)
    
    while not rospy.is_shutdown():
        msg = Twist()
        msg.linear.x = 0.5
        msg.angular.z = 0.5
        pub.publish(msg)
        rate.sleep()

if __name__ == '__main__':
    try:
        follow()
    except rospy.ROSInterruptException:
        pass
