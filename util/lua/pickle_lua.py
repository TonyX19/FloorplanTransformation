import numpy as np
import cPickle
import os
import argparse

parser = argparse.ArgumentParser()
parser.add_argument("--filename", type=str, help="unpickled file path")
parser.add_argument("--variable", type=str, help="")


opt = parser.parse_args()
print(opt.filename)

with open(opt.filename, "wb") as outfile:
    cPickle.dump(opt.variable, outfile, protocol=cPickle.HIGHEST_PROTOCOL)