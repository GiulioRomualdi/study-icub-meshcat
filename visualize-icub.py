
import pinocchio as pin
import numpy as np
import sys
import os
import argparse
from os.path import dirname, join, abspath

from pinocchio.visualize import MeshcatVisualizer

if __name__ == "__main__":

    parser = argparse.ArgumentParser(description='Spawn an icub model.')
    parser.add_argument('-m', '--model', type=str, help='Name of the model. The default value is iCubGazeboV2_5', default="iCubGazeboV2_5")
    args = parser.parse_args()

    # Load the URDF model.
    # Conversion with str seems to be necessary when executing this file with ipython
    model_dir = join(os.environ['CONDA_PREFIX'],"share","iCub")
    if os.name == 'nt':
        model_dir = join(os.environ['CONDA_PREFIX'],"Library","share","iCub")

    model_path = join(model_dir,"robots",args.model)
    mesh_dir = join(model_dir,"meshes", "simmechanics")
    urdf_filename = "model.urdf"
    urdf_model_path = join(model_path, urdf_filename)

    model, collision_model, visual_model = pin.buildModelsFromUrdf(urdf_model_path, mesh_dir, pin.JointModelFreeFlyer())

    viz = MeshcatVisualizer(model, collision_model, visual_model)

    # Start a new MeshCat server and client.
    # Note: the server can also be started separately using the "meshcat-server" command in a terminal:
    # this enables the server to remain active after the current script ends.
    #
    # Option open=True pens the visualizer.
    # Note: the visualizer can also be opened seperately by visiting the provided URL.
    try:
        viz.initViewer(open=True)
    except ImportError as err:
        print("Error while initializing the viewer. It seems you should install Python meshcat")
        print(err)
        sys.exit(0)

    viz.loadViewerModel()
    print("Press enter to close the application")
    input()


