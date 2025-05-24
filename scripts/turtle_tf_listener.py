#!/usr/bin/env python
import rospy
import tf
import math
from turtlesim.srv import Spawn
from geometry_msgs.msg import Twist

def spawn_turtle():
    rospy.wait_for_service('spawn')
    try:
        spawn_turtle = rospy.ServiceProxy('spawn', Spawn)
        response = spawn_turtle(4.0, 2.0, 0.0, "turtle2")
        rospy.loginfo("Вторая черепашка успешно создана: %s", response.name)
        return True
    except rospy.ServiceException as e:
        rospy.logerr("Не удалось создать вторую черепашку: %s", e)
        return False

if __name__ == '__main__':
    rospy.init_node('turtle_tf_listener')
    
    # Попробовать создать черепашку до 3 раз при необходимости
    for i in range(3):
        if spawn_turtle():
            break
        rospy.sleep(1)
    else:
        rospy.logerr("Не удалось создать черепашку после 3 попыток")
        exit(1)
    
    # Публикатор команд движения для turtle2
    turtle_vel = rospy.Publisher('turtle2/cmd_vel', Twist, queue_size=1)
    
    # Слушатель трансформаций tf
    listener = tf.TransformListener()
    
    # Подождать, пока трансформации станут доступны
    rospy.sleep(2)
    listener.waitForTransform('/turtle2', '/carrot_turtle1', rospy.Time(), rospy.Duration(4.0))
    
    rate = rospy.Rate(10)
    while not rospy.is_shutdown():
        try:
            (trans, rot) = listener.lookupTransform('/turtle2', '/carrot_turtle1', rospy.Time(0))
        except (tf.LookupException, tf.ConnectivityException, tf.ExtrapolationException) as e:
            rospy.logwarn("Ошибка при получении трансформации: %s", e)
            rate.sleep()
            continue
        
        # Расчёт угловой и линейной скоростей
        angular = 4 * math.atan2(trans[1], trans[0])
        linear = 0.5 * math.sqrt(trans[0]**2 + trans[1]**2)
        
        # Отправка команды движения
        cmd = Twist()
        cmd.linear.x = linear
        cmd.angular.z = angular
        turtle_vel.publish(cmd)
        
        rate.sleep()




