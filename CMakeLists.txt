cmake_minimum_required(VERSION 2.8.3)
project(keyboard_publisher)
catkin_python_setup()

find_package(catkin REQUIRED COMPONENTS
        rospy
        roscpp
        std_msgs
        message_generation)

add_message_files(
        FILES
        KeyEvent.msg
)

generate_messages(
        DEPENDENCIES
        std_msgs
)

catkin_package(
        CATKIN_DEPENDS
        message_runtime)


catkin_install_python(PROGRAMS
        scripts/key_publisher_node.py
        scripts/key_to_twist_node.py
        DESTINATION ${CATKIN_PACKAGE_SHARE_DESTINATION}/src
        )
install(FILES
        launch/key_publisher.launch
        DESTINATION ${CATKIN_PACKAGE_SHARE_DESTINATION}/launch
        )