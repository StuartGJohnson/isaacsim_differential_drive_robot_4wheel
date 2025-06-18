import unittest
#from scripts.differential_controller_multi_axle import DifferentialControllerMultiAxle
from isaacsim import SimulationApp
import faulthandler
import numpy as np


class MyTestCase(unittest.TestCase):
    def test_faulthandler(self):
        # this breaks all unit test runners. Dammit, NVIDIA!
        self.assertRaises(BaseException, faulthandler.enable)
        #faulthandler.dump_traceback()

    @unittest.skip("can be very useful in pycharm!")
    def test_startup(self):
        simulation_app = SimulationApp({"headless": False})
        simulation_app.close()

    @unittest.skip("can be very useful in pycharm!")
    def test_robot_grab(self):
        simulation_app = SimulationApp({"headless": False})
        import numpy as np
        from isaacsim.core.api import World
        from isaacsim.robot.wheeled_robots.robots import WheeledRobot
        from isaacsim.core.utils.stage import add_reference_to_stage
        world = World(stage_units_in_meters=1.0)
        add_reference_to_stage("usd_assets/world.usda", "/World")
        robot = WheeledRobot(
            prim_path="/World/robot",
            name="robot",
            wheel_dof_names=["left_wheel_joint", "left_wheel2_joint", "right_wheel_joint", "right_wheel2_joint"]
        )
        simulation_app.close()

if __name__ == '__main__':
    unittest.main()
