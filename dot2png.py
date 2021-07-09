#!/usr/bin/env python3
# coding: utf-8
# author: github.com/vuiseng9
# dependency ubt1804: graphviz libgraphviz-dev libgl1-mesa-glx

import os, sys
import pydotplus
from glob import glob
from natsort import natsorted

def dot2png(dotfile, pngfile=None):
    if pngfile is None:
        pngfile = dotfile
        if dotfile.endswith(".dot"):
            pngfile = pngfile.replace('.dot', '.png')
        else:
            pngfile += '.png'
    dotgraph=pydotplus.graph_from_dot_file(dotfile)
    print("[dot2png]: writing ... {}".format(pngfile))
    dotgraph.write_png(pngfile)

if len(sys.argv) != 2:
    raise ValueError("Invalid number of arguments; {}. Usage: dot2png.py <.dot or directory>".format(len(sys.argv)))

target = sys.argv[1]

if os.path.isfile(target) and target.endswith('.dot'):
    dot2png(target)
elif os.path.isdir(target):
    for root, dirs, files in os.walk(target):
        for file in natsorted(files):
            if file.endswith('.dot'):
                dot2png('/'.join([root, file]))
else:
    raise ValueError("Input is not a dot file nor a directory. Usage: dot2png.py <.dot or directory>")

