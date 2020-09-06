import sys
import os
import argparse

sys.path.append(os.getcwd())

parser = argparse.ArgumentParser()
parser.add_argument("--experiment_num", type=str, default="0")

args = parser.parse_args()

from main_atomic import main
main(args.experiment_num)