import os.path
import sys

save_path = '/Users/nbhushan/Desktop'
filepath = os.path.join(save_path, 'a.py')
with open(filepath, "a") as f:
	lines = f.readlines()