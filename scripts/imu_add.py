import omni.graph.core as og

def add_imu(graph_path = "/ActionGraph/ImuPublishGraph"):
    (graph, _, _, _) = og.Controller.edit(
        graph_path,
        {
            og.Controller.Keys.CREATE_NODES: [
                ("onPlayBackTick","omni.graph.action.OnPlaybackTick"),
                ("simStep","isaacsim.core.nodes.OgnIsaacRunOneSimulationFrame"),
                ("readIMU", "isaacsim.sensors.physics.IsaacReadIMU"),
                ("ros2ImuPub", "isaacsim.ros2.bridge.ROS2PublishImu"),
                ("isaac_read_simulation_time", "isaacsim.core.nodes.IsaacReadSimulationTime"),
            ],
            og.Controller.Keys.SET_VALUES: [
                ("readIMU.inputs:imuPrim", "/World/differential_drive_robot_4wheel/base_footprint/base_link/Imu_Sensor"),
                ("ros2ImuPub.inputs:topicName", "/imu"),
                ("ros2ImuPub.inputs:frameId", "base_link"),
            ],
            og.Controller.Keys.CONNECT: [
                ("onPlayBackTick.outputs:tick","simStep.inputs:execIn"),
                ("simStep.outputs:step","readIMU.inputs:execIn"),
                ("readIMU.outputs:execOut", "ros2ImuPub.inputs:execIn"),
                ("readIMU.outputs:orientation", "ros2ImuPub.inputs:orientation"),
                ("readIMU.outputs:angVel", "ros2ImuPub.inputs:angularVelocity"),
                ("readIMU.outputs:linAcc", "ros2ImuPub.inputs:linearAcceleration"),
                ("isaac_read_simulation_time.outputs:simulationTime", "ros2ImuPub.inputs:timeStamp")
            ]
        }
    )

#graph.evaluation_mode = og.GraphEvaluationMode.GRAPH_EVALUATION_MODE_INSTANCED

