#!/usr/bin/env python
import rospy
import tf
import math
from geometry_msgs.msg import Twist

if __name__ == '__main__':
    rospy.init_node('turtle_follower')
    
    listener = tf.TransformListener()
    pub = rospy.Publisher('turtle2/cmd_vel', Twist, queue_size=1)
    rate = rospy.Rate(10.0)
    
    rospy.loginfo("Waiting for turtle2 to be available...")
    listener.waitForTransform("turtle2", "world", rospy.Time(), rospy.Duration(10.0))
    rospy.loginfo("turtle2 is now available!")
    
    while not rospy.is_shutdown():
        try:
            now = rospy.Time.now()
            if listener.canTransform("turtle2", "carrot", now):
                (trans, rot) = listener.lookupTransform("turtle2", "carrot", now)
                
                msg = Twist()
                msg.linear.x = 0.5 * math.sqrt(trans[0]**2 + trans[1]**2)
                msg.angular.z = 4 * math.atan2(trans[1], trans[0])
                pub.publish(msg)
            else:
                rospy.logwarn("Cannot transform from turtle2 to carrot yet...")
                
        except (tf.Exception, rospy.ROSInterruptException) as e:
            rospy.logerr("TF Error: %s", str(e))
            continue
            
        rate.sleep()
