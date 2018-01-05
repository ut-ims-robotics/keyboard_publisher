from pykeyboard import PyKeyboardEvent
from threading import Thread

from keyboard_publisher.msg import KeyEvent

import rospy


class KeyPublisher(PyKeyboardEvent):
    def __init__(self):
        PyKeyboardEvent.__init__(self)

        self.key_pub = rospy.Publisher("keyboard_publisher/key_event", KeyEvent, queue_size=10)

        self.thread = Thread(target=self.run)
        self.thread.start()

    def tap(self, keycode, character, press):
        key_event_msg = KeyEvent()
        key_event_msg.keyCode = keycode
        key_event_msg.char = str(character)
        key_event_msg.pressed = press
        self.key_pub.publish(key_event_msg)

    def stop(self):
        super(KeyPublisher, self).stop()
        self.thread.join()
