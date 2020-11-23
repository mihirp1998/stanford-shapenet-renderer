import meshio
import math, sys, random, argparse, json, os, tempfile, pickle
import shutil
import subprocess
import os
import numpy as np
import time
from subprocess import Popen, PIPE
import shlex
import sys 




off_folder = "/home/mprabhud/ishita/convocc/convolutional_occupancy_networks/out/pointcloud/shapenet_grid32/generation_pretrained/meshes/02933112"
outfolder = "/home/mprabhud/ishita/convocc/convolutional_occupancy_networks/out/pointcloud/shapenet_grid32/generation_pretrained/meshes_obj"
render_dir = "/home/mprabhud/ishita/convocc/convolutional_occupancy_networks/out/pointcloud/shapenet_grid32/generation_pretrained/render"

#meshes to render
files_to_use = ['b6b378a05bf6982b70c33714b19283df', 'e16c0191973a25f02d63c890dc92b5', 'e2d06603fba3bf3310af74324aae27f',
'b7a9d8b469cb06037824b732b006daaa', 'e22f10f551cac7fc6cb99ff1a702c4e9', 'eaf341c056c79bec1a2c782fdbf60db6']

for mesh_file in files_to_use:
    
    if '.ipynb' in mesh_file:
        continue
    
    mesh = meshio.read(
        os.path.join(off_folder, mesh_file+'.off'),  # string, os.PathLike, or a buffer/open file
    )

    meshio.write(
        os.path.join(outfolder, mesh_file+'.obj'),
        mesh,
    )
    
    ot_file = os.path.join(outfolder, mesh_file+'.obj')
    render_file = os.path.join(render_dir)
    
    blender_command = f'blender --background --python render_blender.py -- --output_folder {render_file} {ot_file} --format OPEN_EXR --color_depth 16 --scale 2.5'
    blender_command_args = shlex.split(blender_command)
    p1 = Popen(blender_command_args, stdout=PIPE, stderr=PIPE)
    time.sleep(0.1)
    out, err = p1.communicate()
