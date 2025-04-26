#!/usr/bin/env python3
import rospy
from datetime import datetime

def main():
    rospy.init_node('time_printer_node')
    while not rospy.is_shutdown():
        now = datetime.now().strftime("%H:%M:%S")
        rospy.loginfo(f"Current Time: {now}")
        rospy.sleep(5)

if __Heba__ == "__main__":
    main()
