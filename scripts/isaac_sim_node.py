#!/usr/bin/env python3
# 2025 Stuart Johnson
#
# The core robot simulator as a ros2 node. This node subscribes to robot twist
# commands and steps the robot simulation. Initialization includes spin-up of
# all sensors.
#
import time
import rclpy
from rclpy.node import Node
import os
import yaml
import numpy as np
from ament_index_python.packages import get_package_share_directory

from isaacsim import SimulationApp

class IsaacSimNode(Node):
    def __init__(self):
        super().__init__('isaac_sim_node')
        self.simulation_app = SimulationApp({"headless": True})

        from isaacsim.core.api import SimulationContext
        from isaacsim.core.utils.extensions import enable_extension
        from isaacsim.core.api import World
        import omni.usd
        from pxr import Usd, UsdGeom, Gf, Sdf

        enable_extension("isaacsim.ros2.bridge")

        self.simulation_app.update()

        default_world_file = ""
        self.declare_parameter('world', default_world_file) # Declare the parameter with a default value
        world_file = self.get_parameter('world').get_parameter_value().string_value

        print('world file is: ', world_file)

        omni.usd.get_context().open_stage(world_file, None)
        stage = omni.usd.get_context().get_stage()

        # retrieve robot_start_xy from world definition
        # strip extension from path
        world_file_root = os.path.splitext(world_file)[0]
        cfg_world_path = world_file_root + '.yml'

        with open(cfg_world_path, 'r') as file:
            data = yaml.safe_load(file)
        robot_start_xy = np.array(data['robot_start_xy'])

        # note we are assuming our robot name - this applies in action graph
        # definition below as well
        robot_prim = "/World/differential_drive_robot_4wheel"
        prim = stage.DefinePrim("/World/differential_drive_robot_4wheel", "Xform")

        pkg_name = "isaacsim_differential_drive_robot_4wheel"
        pkg_dir = get_package_share_directory(pkg_name)
        robot_path = os.path.join(pkg_dir, "usd_assets", "robot.usda")

        # load the robot into the scene
        prim.GetReferences().AddReference(robot_path)

        # set the robot initial position
        robot_prim_thingy = stage.GetPrimAtPath(robot_prim)
        if not robot_prim_thingy.IsValid():
            print("Invalid prim!")
        else:
            print("Valid prim.")
        xformable = UsdGeom.Xformable(robot_prim_thingy)

        # Get all transform ops (translate, rotate, scale)
        xform_ops = xformable.GetOrderedXformOps()

        # Find the translate op and modify it
        found_rotate = False
        for op in xform_ops:
            if op.GetOpType() == UsdGeom.XformOp.TypeTranslate:
                op.Set(Gf.Vec3d(robot_start_xy[0], robot_start_xy[1], 0.25))
            elif op.GetOpType() == UsdGeom.XformOp.TypeRotateXYZ:
                op.Set(Gf.Vec3d(0, 0, 0))
                found_rotate = True
        if not found_rotate:
            rotate_op = xformable.AddRotateXYZOp()
            rotate_op.Set(Gf.Vec3f(0, 0, 0))

        self.simulation_context = SimulationContext(physics_dt=1.0 / 60.0, rendering_dt=1.0 / 60.0,
                                              stage_units_in_meters=1.0)
        #self.world = World()
        # world.reset()
        #self.world.play()
        #self.simulation_context.initialize_physics()
        self.simulation_context.play()

        self.simulation_app.update()
        self.simulation_app.update()

        # construct ros2 publishers and subscribers (action graphs)
        from controller_add import add_controller
        from tf_lidar_add import add_tf_lidar
        #from lidar_add import add_lidar
        #from all_tf_add import add_all_tf
        from imu_add import add_imu
        from depth_camera_add import add_depth_camera
        from rgb_camera_add import add_rgb_camera

        add_tf_lidar()
        add_controller()
        add_imu()
        add_depth_camera()
        add_rgb_camera()
        #add_all_tf()

        self.simulation_app.update()
        self.simulation_app.update()

        self.timer = self.create_timer(1.0/60.0, self.step)

    def step(self):
        self.simulation_app.update()
        #self.simulation_context.step(render=True)
        #time.sleep(1.0/60.0)

    def destroy_node(self):
        super().destroy_node()
        self.simulation_context.stop()
        self.simulation_app.close()

def main(args=None):
    rclpy.init(args=args)
    node = IsaacSimNode()
    try:
        rclpy.spin(node)
    except KeyboardInterrupt:
        pass
    node.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()

