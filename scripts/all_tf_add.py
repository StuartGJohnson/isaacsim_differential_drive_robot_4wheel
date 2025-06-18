import omni.graph.core as og

def add_all_tf(graph_path = "/ActionGraph/TFPublishGraph"):
    og.Controller.edit(
        graph_path,
        {
            og.Controller.Keys.CREATE_NODES: [
                ("on_playback_tick", "omni.graph.action.OnPlaybackTick"),
                ("sim_step","isaacsim.core.nodes.OgnIsaacRunOneSimulationFrame"),
                ("isaac_read_simulation_time", "isaacsim.core.nodes.IsaacReadSimulationTime"),
                ("ros2_publish_transform_tree", "isaacsim.ros2.bridge.ROS2PublishTransformTree"),
                ("ros2_publish_odometry", "isaacsim.ros2.bridge.ROS2PublishOdometry"),
                ("ros2_publish_raw_transform_tree", "isaacsim.ros2.bridge.ROS2PublishRawTransformTree"),
                ("ros2_publish_raw_transform_tree2", "isaacsim.ros2.bridge.ROS2PublishRawTransformTree"),
                ("isaac_compute_odometry_node", "isaacsim.core.nodes.IsaacComputeOdometry")
            ],
            og.Controller.Keys.SET_VALUES: [
                #("ros2_publish_transform_tree.inputs:nodeNamespace", ""),
                ("ros2_publish_transform_tree.inputs:topicName", "tf"),
                ("ros2_publish_transform_tree.inputs:parentPrim", "/World"),
                ("ros2_publish_transform_tree.inputs:targetPrims", ["/World/differential_drive_robot_4wheel"]),
                ("ros2_publish_odometry.inputs:chassisFrameId", "body_link"),
                ("ros2_publish_odometry.inputs:odomFrameId", "odom"),
                ("ros2_publish_odometry.inputs:topicName", "odom"),
                ("ros2_publish_raw_transform_tree.inputs:childFrameId", "base_footprint"),
                ("ros2_publish_raw_transform_tree.inputs:parentFrameId", "odom"),
                ("ros2_publish_raw_transform_tree.inputs:topicName", "tf"),
                ("ros2_publish_raw_transform_tree2.inputs:childFrameId", "odom"),
                ("ros2_publish_raw_transform_tree2.inputs:parentFrameId", "World"),
                ("ros2_publish_raw_transform_tree2.inputs:topicName", "tf"),
                ("isaac_compute_odometry_node.inputs:chassisPrim", "/World/differential_drive_robot_4wheel"),
            ],
            og.Controller.Keys.CONNECT: [
                ("on_playback_tick.outputs:tick", "sim_step.inputs:execIn"),
                ("sim_step.outputs:step", "ros2_publish_transform_tree.inputs:execIn"),
                ("isaac_read_simulation_time.outputs:simulationTime", "ros2_publish_transform_tree.inputs:timeStamp"),
                ("sim_step.outputs:step", "isaac_compute_odometry_node.inputs:execIn"),
                ("isaac_compute_odometry_node.outputs:execOut", "ros2_publish_odometry.inputs:execIn"),
                ("isaac_compute_odometry_node.outputs:execOut", "ros2_publish_raw_transform_tree.inputs:execIn"),
                ("isaac_compute_odometry_node.outputs:execOut", "ros2_publish_raw_transform_tree2.inputs:execIn"),
                ("isaac_read_simulation_time.outputs:simulationTime", "ros2_publish_odometry.inputs:timeStamp"),
                ("isaac_read_simulation_time.outputs:simulationTime", "ros2_publish_raw_transform_tree.inputs:timeStamp"),
                ("isaac_read_simulation_time.outputs:simulationTime", "ros2_publish_raw_transform_tree2.inputs:timeStamp"),
                ("isaac_compute_odometry_node.outputs:linearVelocity", "ros2_publish_odometry.inputs:linearVelocity"),
                ("isaac_compute_odometry_node.outputs:angularVelocity", "ros2_publish_odometry.inputs:angularVelocity"),
                ("isaac_compute_odometry_node.outputs:orientation", "ros2_publish_odometry.inputs:orientation"),
                ("isaac_compute_odometry_node.outputs:position", "ros2_publish_odometry.inputs:position"),
                ("isaac_compute_odometry_node.outputs:orientation", "ros2_publish_raw_transform_tree.inputs:rotation"),
                ("isaac_compute_odometry_node.outputs:position", "ros2_publish_raw_transform_tree.inputs:translation"),
            ]
        }
    )