from pxr import Usd

package_dir = "/home/sjohnson/ros2_ws/src/isaacsim_differential_drive_robot_4wheel/"
world_dir = "/home/sjohnson/WorldGeneration/"

robot_path = package_dir + "usd_assets/robot.usda"

stage = Usd.Stage.Open(robot_path)
print("Default prim:", stage.GetDefaultPrim())

print("Top-level prims in file:")
for prim in stage.GetPseudoRoot().GetChildren():
    print(prim.GetPath())
    # Check for references on this prim
    if prim.HasAuthoredReferences():
        print("  Has references:")
        print("   ", prim.GetReferences().GetAddedOrExplicitItems())

for prim in stage.Traverse():
    print(prim.GetPath())

# from pxr import Sdf
#
# layer = Sdf.Layer.FindOrOpen(robot_path)
# print(layer.subLayerPaths)  # SubLayer references
# print(layer.references)  # Direct references