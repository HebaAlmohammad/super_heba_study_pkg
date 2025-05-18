#!/usr/bin/env python
import rospy
import tf
import math
from geometry_msgs.msg import Twist

if __name__ == '__main__':
    rospy.init_node('tf_turtle_follower')
    
    listener = tf.TransformListener()
    turtle_vel = rospy.Publisher('turtle2/cmd_vel', Twist, queue_size=1)
    
    rate = rospy.Rate(10.0)
    rospy.loginfo("Starting turtle follower... Please wait 10 seconds...")
    
    # Wait for all transforms to be available
    rospy.sleep(10.0)
    
    while not rospy.is_shutdown():
        try:
            now = rospy.Time.now()
            if listener.canTransform("turtle2", "carrot", now):
                (trans, rot) = listener.lookupTransform("turtle2", "carrot", now)
                
                msg = Twist()
                msg.linear.x = 0.5 * math.sqrt(trans[0]**2 + trans[1]**2)
                msg.angular.z = 4 * math.atan2(trans[1], trans[0])
                turtle_vel.publish(msg)
            else:
                rospy.logwarn("Cannot find transform between turtle2 and carrot")
                
        except (tf.LookupException, tf.ConnectivityException, 
                tf.ExtrapolationException) as e:
            rospy.logerr("TF Error: %s", str(e))
            continue
            
        rate.sleep()
