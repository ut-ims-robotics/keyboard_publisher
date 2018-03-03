#!/usr/bin/env python

import rospy
from keyboard_publisher.key_listener import KeyListener
from geometry_msgs.msg import TwistStamped
from keyboard_publisher.msg import KeyEvent


class KeyToTwist(KeyListener):
    def __init__(self):
        KeyListener.__init__(self)
        self.twist_pub = rospy.Publisher('jog_arm_server/delta_jog_cmds', TwistStamped, queue_size=1)
        rospy.Subscriber("keyboard_publisher/key_event", KeyEvent, self.callback)
        self.twist_msg = TwistStamped()

    def callback(self, key_event_msg):
        pressed = False
        if key_event_msg.pressed:
            pressed = True

        self.twist_msg.header.stamp = rospy.Time.now()
        self.twist_msg.header.frame_id = rospy.get_param("joy_to_twist/cmd_frame", "/cmd_frame")

        self.twist_msg.twist.linear.x = 0
        self.twist_msg.twist.linear.y = 0
        self.twist_msg.twist.linear.z = 0
        self.twist_msg.twist.angular.x = 0
        self.twist_msg.twist.angular.y = 0
        self.twist_msg.twist.angular.z = 0

        if key_event_msg.char == "w":  # forward
            if pressed:
                self.twist_msg.twist.linear.x = 0.2
            self.twist_pub.publish(self.twist_msg)

        if key_event_msg.char == "s":  # backward
            if pressed:
                self.twist_msg.twist.linear.x = -0.2
            self.twist_pub.publish(self.twist_msg)

        if key_event_msg.char == "d":
            if pressed:
                self.twist_msg.twist.linear.y = 0.2
            self.twist_pub.publish(self.twist_msg)

        if key_event_msg.char == "a":
            if pressed:
                self.twist_msg.twist.linear.y = -0.2
            self.twist_pub.publish(self.twist_msg)




if __name__ == '__main__':
    try:
        rospy.init_node("key_to_twist_node")
        rate = rospy.Rate(100)
        key_publisher = KeyToTwist()

        while not rospy.is_shutdown():
            rate.sleep()

    except rospy.ROSInterruptException:
        pass
