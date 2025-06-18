import omni.graph.core as og

def add_depth_camera(graph_path = "/ActionGraph/DepthPublishGraph"):
    og.Controller.edit(graph_path, {
        og.Controller.Keys.CREATE_NODES: [
            ("onTick", "omni.graph.action.OnPlaybackTick"),
            ("runOnce", "isaacsim.core.nodes.OgnIsaacRunOneSimulationFrame"),
            ("cameraHelperRgb", "isaacsim.ros2.bridge.ROS2CameraHelper"),
            ("ros2_qos_profile", "isaacsim.ros2.bridge.ROS2QoSProfile"),
            ("create_render_product", "isaacsim.core.nodes.IsaacCreateRenderProduct"),
            #("cameraHelperInfo", "isaacsim.ros2.bridge.ROS2CameraInfoHelper"),
        ],
        og.Controller.Keys.SET_VALUES: [
            ("cameraHelperRgb.inputs:frameId", "d435_link"),
            ("cameraHelperRgb.inputs:topicName", "depth"),
            ("cameraHelperRgb.inputs:type", "depth"),
            ("cameraHelperRgb.inputs:nodeNamespace", "depth_camera"),
            #("cameraHelperInfo.inputs:frameId", "d435_link"),
            #("cameraHelperInfo.inputs:topicName", "camera_info"),
            #("cameraHelperInfo.inputs:nodeNamespace", "rgb_camera"),
            ("create_render_product.inputs:cameraPrim", "/World/differential_drive_robot_4wheel/base_footprint/d435_link/Depth_Camera"),
            #("cameraHelperRgb.inputs:renderProductPath", "/World/differential_drive_robot_4wheel/d435_link/RGB_Camera_Output"),
            #("cameraHelperInfo.inputs:renderProductPath", "/World/differential_drive_robot_4wheel/d435_link/RGB_Camera_Output"),
        ],
        og.Controller.Keys.CONNECT: [
            ("onTick.outputs:tick", "runOnce.inputs:execIn"),
            #("runOnce.outputs:step", "cameraHelperRgb.inputs:execIn"),
            ("runOnce.outputs:step", "create_render_product.inputs:execIn"),
            ("create_render_product.outputs:execOut", "cameraHelperRgb.inputs:execIn"),
            ("create_render_product.outputs:renderProductPath", "cameraHelperRgb.inputs:renderProductPath"),
            ("ros2_qos_profile.outputs:qosProfile", "cameraHelperRgb.inputs:qosProfile")
            #("runOnce.outputs:step", "cameraHelperInfo.inputs:execIn"),
        ]
    })