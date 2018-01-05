#!/usr/bin/env python

import rospy
from keyboard_publisher.key_pub import KeyPublisher

if __name__ == '__main__':
    try:
        rospy.init_node("key_publisher_node")

        rate = rospy.Rate(20)

        key_publisher = KeyPublisher()

        rospy.loginfo("key_publisher_node started listening keys")
        while not rospy.is_shutdown():
            rate.sleep()

        key_publisher.stop()
        rospy.loginfo("key_publisher_node stopped")

    except rospy.ROSInterruptException:
        pass
