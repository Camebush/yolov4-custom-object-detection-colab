import os
import numpy as np
# Current directory
current_dir = 'data/object'

# Percentage of images to be used for the test set
test_ratio = 0.15

# Valide image files we will use
valid_extensions = [".jpg",".gif",".png",".jpeg"]

allfilenames = [filename for filename in os.listdir(current_dir) if os.path.splitext(filename)[1].lower() in valid_extensions]
np.random.shuffle(allfilenames)

train_FileNames , test_FileNames = np.split(np.array(allfilenames), [int(len(allfilenames)*(1-test_ratio))])

train_FileNames = [current_dir + '/' + name for name in train_FileNames.tolist()]
test_FileNames = [current_dir + '/' + name for name in test_FileNames.tolist()]

with open('data/train.txt', 'w') as train_f:
    for name in train_FileNames:
        train_f.write(name+'\n')

with open('data/test.txt', 'w') as test_f:
    for name in test_FileNames:
        test_f.write(name+'\n')