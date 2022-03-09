import argparse
import glob
import os
import random

import numpy as np
import shutil

from utils import get_module_logger


def split(data_dir):
    """
    Create three splits from the processed records. The files should be moved to new folders in the 
    same directory. This folder should be named train, val and test.

    args:
        - data_dir [str]: data directory, /home/workspace/data/waymo
    """
    
    # TODO: Split the data present in `/home/workspace/data/waymo/training_and_validation` into train and val sets.
    # You should move the files rather than copy because of space limitations in the workspace.
    source_dir = data_dir + '/training_and_validation/'
    train_dir = data_dir + '/train/'
    val_dir = data_dir + '/val/'
    file_count = 0
    for filepath in glob.iglob(source_dir + '/*'):
        file_count += 1
      
    # 90% training 10% validation
    train_count = file_count * 90 // 100
    # val_count = file_count - train_count
    
    count = 0
    for file_name in os.listdir(source_dir):
        if(count < train_count):
            shutil.move(source_dir + file_name, train_dir + file_name)
            count = count + 1
        else:
            shutil.move(source_dir + file_name, val_dir + file_name)
        
if __name__ == "__main__": 
    parser = argparse.ArgumentParser(description='Split data into training / validation / testing')
    parser.add_argument('--data_dir', required=True,
                        help='data directory')
    args = parser.parse_args()

    logger = get_module_logger(__name__)
    logger.info('Creating splits...')
    split(args.data_dir)