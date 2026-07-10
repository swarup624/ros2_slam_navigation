cmake_minimum_required(VERSION 3.8)
project(my_robot_navigation)

find_package(ament_cmake REQUIRED)

install(
    DIRECTORY
        launch
        config
        maps
        rviz
        scripts
    DESTINATION share/${PROJECT_NAME}
)

install(PROGRAMS
    scripts/waypoint_navigation.py
    DESTINATION lib/${PROJECT_NAME}
)

ament_package()