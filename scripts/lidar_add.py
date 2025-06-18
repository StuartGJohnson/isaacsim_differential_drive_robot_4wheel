import omni.graph.core as og

def add_lidar(graph_path = "/ActionGraph/LidarPublishGraph"):
    og.Controller.edit(
        graph_path,
        {
            og.Controller.Keys.CREATE_NODES: [
                ("onTick", "omni.graph.action.OnPlaybackTick"),
                ("runOnce", "isaacsim.core.nodes.OgnIsaacRunOneSimulationFrame"),
                ("readLidar", "isaacsim.sensors.physx.IsaacReadLidarBeams"),
                ("ros2PubLidar", "isaacsim.ros2.bridge.ROS2PublishLaserScan"),
                ("isaac_read_simulation_time", "isaacsim.core.nodes.IsaacReadSimulationTime"),
            ],
            og.Controller.Keys.SET_VALUES: [
                ("readLidar.inputs:lidarPrim", "/World/differential_drive_robot_4wheel/base_footprint/lidar_link/Lidar"),
                ("ros2PubLidar.inputs:topicName", "/scan"),
                ("ros2PubLidar.inputs:frameId", "lidar_link")
            ],
            og.Controller.Keys.CONNECT: [
                ("onTick.outputs:tick", "runOnce.inputs:execIn"),
                ("runOnce.outputs:step", "readLidar.inputs:execIn"),
                ("readLidar.outputs:execOut", "ros2PubLidar.inputs:execIn"),
                ("readLidar.outputs:depthRange", "ros2PubLidar.inputs:depthRange"),
                ("readLidar.outputs:azimuthRange", "ros2PubLidar.inputs:azimuthRange"),
                ("readLidar.outputs:horizontalFov", "ros2PubLidar.inputs:horizontalFov"),
                ("readLidar.outputs:horizontalResolution", "ros2PubLidar.inputs:horizontalResolution"),
                ("readLidar.outputs:intensitiesData", "ros2PubLidar.inputs:intensitiesData"),
                ("readLidar.outputs:linearDepthData", "ros2PubLidar.inputs:linearDepthData"),
                ("readLidar.outputs:numCols", "ros2PubLidar.inputs:numCols"),
                ("readLidar.outputs:numRows", "ros2PubLidar.inputs:numRows"),
                ("readLidar.outputs:rotationRate", "ros2PubLidar.inputs:rotationRate"),
                ("isaac_read_simulation_time.outputs:simulationTime", "ros2PubLidar.inputs:timeStamp")
            ]
        }
    )

