#!/usr/bin/env python
import rospy
import tf
import math
from geometry_msgs.msg import Twist

if __name__ == '__main__':
    rospy.init_node('moving_carrot')
    br = tf.TransformBroadcaster()
    rate = rospy.Rate(10.0)
    
    while not rospy.is_shutdown():
        t = rospy.Time.now().to_sec() * 0.5  
        x = 0.3 * math.cos(t)
        y = 0.3 * math.sin(t)
        
        br.sendTransform((x, y, 0),
                        tf.transformations.quaternion_from_euler(0, 0, 0),
                        rospy.Time.now(),
                        "carrot",
                        "turtle1")
        rate.sleep()
