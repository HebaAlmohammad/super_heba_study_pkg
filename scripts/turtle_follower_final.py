#!/usr/bin/env python
import rospy
import tf
import math
from geometry_msgs.msg import Twist

if __name__ == '__main__':
    rospy.init_node('turtle_follower_final', log_level=rospy.DEBUG)
    
    listener = tf.TransformListener()
    pub = rospy.Publisher('turtle2/cmd_vel', Twist, queue_size=1)
    rate = rospy.Rate(10.0)
    
    rospy.loginfo("Waiting for transforms to become available...")
    
    # انتظار حتى تصبح جميع التحويلات متاحة
    listener.waitForTransform("turtle2", "world", rospy.Time(), rospy.Duration(10.0))
    listener.waitForTransform("turtle1", "carrot", rospy.Time(), rospy.Duration(10.0))
    
    rospy.loginfo("All transforms available. Starting follower...")
    
    while not rospy.is_shutdown():
        try:
            now = rospy.Time.now()
            
            
            if (listener.canTransform("turtle2", "carrot", now) and 
                listener.canTransform("turtle1", "carrot", now)):
                
                (trans, rot) = listener.lookupTransform("turtle2", "carrot", now)
                
                msg = Twist()
                msg.linear.x = 0.5 * math.sqrt(trans[0]**2 + trans[1]**2)
                msg.angular.z = 4 * math.atan2(trans[1], trans[0])
                
                pub.publish(msg)
                rospy.logdebug("Published command: linear=%.2f, angular=%.2f", 
                              msg.linear.x, msg.angular.z)
            else:
                rospy.logwarn("Transforms not yet available...")
                
        except (tf.LookupException, tf.ConnectivityException, 
                tf.ExtrapolationException) as e:
            rospy.logerr("TF Error: %s", str(e))
            
        rate.sleep()
