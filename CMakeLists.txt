cmake_minimum_required(VERSION 3.0.2)
project(super_heba_study_pkg)

find_package(catkin REQUIRED COMPONENTS
  rospy
)

catkin_package()

install(DIRECTORY scripts/
  DESTINATION ${CATKIN_PACKAGE_BIN_DESTINATION}
)
