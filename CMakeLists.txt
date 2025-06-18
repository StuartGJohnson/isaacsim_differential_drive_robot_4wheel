cmake_minimum_required(VERSION 3.5)
project(isaacsim_differential_drive_robot_4wheel)

find_package(ament_cmake REQUIRED)
find_package(rclpy REQUIRED)
find_package(geometry_msgs REQUIRED)

install(
  DIRECTORY scripts/
  DESTINATION lib/${PROJECT_NAME}
  USE_SOURCE_PERMISSIONS
)

install(
  DIRECTORY config launch scripts usd_assets
  DESTINATION share/${PROJECT_NAME}
)

#install(PROGRAMS
#    scripts/isaac_sim_node.py
#    scripts/all_tf_add.py
#    scripts/controller_add.py
#    scripts/depth_camera_add.py
#    scripts/imu_add.py
#    scripts/lidar_add.py
#    scripts/rgb_camera_add.py
#    DESTINATION lib/${PROJECT_NAME}
#)

install(
  FILES
    launch/isaac_sim.launch.py
  DESTINATION share/${PROJECT_NAME}/launch
)

ament_package()
