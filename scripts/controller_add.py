import omni.graph.core as og

def add_controller(graph_path = "/ActionGraph/Controller" ):
    keys = og.Controller.Keys
    (graph, nodes, _, _) = og.Controller.edit(
        graph_path,
        {
            keys.CREATE_NODES: [
                ("OnPlaybackTick", "omni.graph.action.OnPlaybackTick"),
                ("ReadSimTime", "isaacsim.core.nodes.IsaacReadSimulationTime"),
                # odometry moved elsewhere, but ...
                #("computeOdom", "isaacsim.core.nodes.IsaacComputeOdometry"),
                #("publishOdom", "isaacsim.ros2.bridge.ROS2PublishOdometry"),
                #("publishRawTF", "isaacsim.ros2.bridge.ROS2PublishRawTransformTree"),
                ("subscribeTwist", "isaacsim.ros2.bridge.ROS2SubscribeTwist"),
                ("breakLinVel", "omni.graph.nodes.BreakVector3"),
                ("breakAngVel", "omni.graph.nodes.BreakVector3"),
                ("diffController", "isaacsim.robot.wheeled_robots.DifferentialController"),
                ("artController", "isaacsim.core.nodes.IsaacArticulationController"),
                ("appendArray", "omni.graph.nodes.AppendArray"),

            ],
            keys.CONNECT: [
                # moved elsewhere
                #("OnPlaybackTick.outputs:tick", "computeOdom.inputs:execIn"),
                #("OnPlaybackTick.outputs:tick", "publishOdom.inputs:execIn"),
                #("OnPlaybackTick.outputs:tick", "publishRawTF.inputs:execIn"),
                #("ReadSimTime.outputs:simulationTime", "publishOdom.inputs:timeStamp"),
                #("ReadSimTime.outputs:simulationTime", "publishRawTF.inputs:timeStamp"),
                #("computeOdom.outputs:angularVelocity", "publishOdom.inputs:angularVelocity"),
                #("computeOdom.outputs:linearVelocity", "publishOdom.inputs:linearVelocity"),
                #("computeOdom.outputs:orientation", "publishOdom.inputs:orientation"),
                #("computeOdom.outputs:position", "publishOdom.inputs:position"),
                #("computeOdom.outputs:orientation", "publishRawTF.inputs:rotation"),
                #("computeOdom.outputs:position", "publishRawTF.inputs:translation"),
                ("OnPlaybackTick.outputs:tick", "subscribeTwist.inputs:execIn"),
                ("OnPlaybackTick.outputs:tick", "artController.inputs:execIn"),
                ("subscribeTwist.outputs:execOut", "diffController.inputs:execIn"),
                ("subscribeTwist.outputs:linearVelocity", "breakLinVel.inputs:tuple"),
                ("breakLinVel.outputs:x", "diffController.inputs:linearVelocity"),
                ("subscribeTwist.outputs:angularVelocity", "breakAngVel.inputs:tuple"),
                ("breakAngVel.outputs:z", "diffController.inputs:angularVelocity"),
                ("diffController.outputs:velocityCommand", "appendArray.inputs:input0"),
                ("diffController.outputs:velocityCommand", "appendArray.inputs:input1"),
                ("appendArray.outputs:array", "artController.inputs:velocityCommand"),
            ],
            og.Controller.Keys.SET_VALUES: [
                ("diffController.inputs:wheelRadius", 0.039),
                ("diffController.inputs:wheelDistance", 0.174*1.62),
                ("artController.inputs:jointNames", ["left_wheel_joint", "right_wheel_joint", "left_wheel2_joint", "right_wheel2_joint"]),
                ("artController.inputs:targetPrim", ["/World/differential_drive_robot_4wheel"]),
                #("publishOdom.inputs:chassisFrameId", "base_link"),
                #("publishOdom.inputs:odomFrameId", "odom"),
                #("publishOdom.inputs:topicName", "odom"),
                #("publishRawTF.inputs:childFrameId", "base_link"),
                #("publishRawTF.inputs:parentFrameId", "odom"),
                #("publishRawTF.inputs:topicName", "tf"),
                #("computeOdom.inputs:chassisPrim", "/World/differential_drive_robot_4wheel"),
            ],
        }
    )