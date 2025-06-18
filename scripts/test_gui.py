
from isaacsim import SimulationApp
simulation_app = SimulationApp({"headless": False})

import omni.usd
from pxr import Usd

# Create an empty stage with a single prim to test
stage = Usd.Stage.CreateNew("test_stage.usda")
stage.DefinePrim("/World/TestCube", "Cube")
stage.SetDefaultPrim(stage.GetPrimAtPath("/World"))
stage.GetRootLayer().Save()

omni.usd.get_context().open_stage("test_stage.usda", None)
stage = omni.usd.get_context().get_stage()

# Load the stage
#stage = Usd.Stage.Open("test_stage.usda")
#simulation_app.play()
# Give GUI time to initialize and show it
for _ in range(100):  # This should run for a few seconds
    simulation_app.update()

simulation_app.close()
