import os
from PIL import Image
import argparse

parser = argparse.ArgumentParser()
parser.add_argument('--dir', help='Location to run script',required=True)

args = parser.parse_args()

count = 0

for i in os.listdir(args.dir):
	i_path = os.path.join(args.dir, i)
	new_i_path = os.path.join(args.dir,'img-'+str(count)+'.'+i.split('.')[-1])
	os.rename(i_path,new_i_path)
	count+=1