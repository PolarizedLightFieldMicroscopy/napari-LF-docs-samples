args = [
    "light_field.png",
    "-c",
    "calibration.lfc",
    "-o",
    "antleg_stack.tif",
    "--solver",
    "rl",
    # "--use-single-precision",
]

import os, sys
currentdir = os.path.dirname(os.path.realpath(__file__))
grandparentdir = os.path.dirname(os.path.dirname(currentdir))
sys.path.append(grandparentdir)
from lfdeconvolve import main

main(args)