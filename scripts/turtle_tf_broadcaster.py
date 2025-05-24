#!/usr/bin/env python
import rospy
import tf
import math
from tf.transformations import quaternion_from_euler
from turtlesim.msg import Pose

def handle_turtle_pose(msg, turtlename):
    br = tf.TransformBroadcaster()
    # Бродкаст преобразования черепахи относительно мира
    br.sendTransform((msg.x, msg.y, 0),
                    quaternion_from_euler(0, 0, msg.theta),
                    rospy.Time.now(),
                    turtlename,
                    "world")
    
    # Бродкаст преобразования морковки, которая вращается вокруг черепахи
    t = rospy.Time.now().to_sec()
    br.sendTransform((0.3 * math.cos(t), 0.3 * math.sin(t), 0),
                    quaternion_from_euler(0, 0, 0),
                    rospy.Time.now(),
                    "carrot_" + turtlename,
                    turtlename)

if __name__ == '__main__':
    rospy.init_node('turtle_tf_broadcaster')
    turtlename = rospy.get_param('~turtle')
    rospy.Subscriber('/%s/pose' % turtlename,
                    Pose,
                    handle_turtle_pose,
                    turtlename)
    rospy.spin()

