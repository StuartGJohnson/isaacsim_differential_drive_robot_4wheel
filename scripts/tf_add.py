import omni.graph.core as og

def add_tf(graph_path = "/ActionGraph/TFPublishGraph"):
    og.Controller.edit(
        graph_path,
        {
            og.Controller.Keys.CREATE_NODES: [
                ("on_playback_tick", "omni.graph.action.OnPlaybackTick"),
                ("sim_step","isaacsim.core.nodes.OgnIsaacRunOneSimulationFrame"),
                ("isaac_read_simulation_time", "isaacsim.core.nodes.IsaacReadSimulationTime"),
                ("ros2_publish_transform_tree", "isaacsim.ros2.bridge.ROS2PublishTransformTree"),
            ],
            og.Controller.Keys.SET_VALUES: [
                #("ros2_publish_transform_tree.inputs:nodeNamespace", ""),
                ("ros2_publish_transform_tree.inputs:topicName", "tf"),
                ("ros2_publish_transform_tree.inputs:parentPrim", "/World"),
                ("ros2_publish_transform_tree.inputs:targetPrims", ["/World/differential_drive_robot_4wheel"]),
            ],
            og.Controller.Keys.CONNECT: [
                ("on_playback_tick.outputs:tick", "sim_step.inputs:execIn"),
                ("sim_step.outputs:step", "ros2_publish_transform_tree.inputs:execIn"),
                ("isaac_read_simulation_time.outputs:simulationTime", "ros2_publish_transform_tree.inputs:timeStamp"),
            ]
        }
    )