from keyboard_publisher.msg import KeyEvent
import rospy


class KeyListener:
    def __init__(self):
        self.key_sub = rospy.Subscriber("keyboard_publisher/key_event", KeyEvent,
                                        self.key_event_callback)

    def key_event_callback(self, key_event_msg):
        pass
