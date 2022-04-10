import matplotlib.pylab as plt
import cv2 
import glob
import os
import argparse
from pathlib import Path
import numpy as np
import shutil


#To Run this script, simply paste the following into the terminal: python move_nii_files_script.py

#This is the location that can be used to actually access the derivatives folder for the verse2020 dataset.

input_dir = "/mnt/batch/tasks/shared/LS_root/mounts/clusters/hbarton72/code/Users/hbarton7/verse_testing_files/derivatives/"


output_dir = "MedicalDataAugmentationTool-VerSe/verse2020/verse2020_dataset/images/"


# trying to access derivatives
verse_files = os.listdir(input_dir) #This is the line to list all folders inside the derivatives folder
print(verse_files)
verse_files = verse_files[1:] 


for verse_file in verse_files:
    vfile = os.listdir(input_dir + verse_file) 
    moveFile = vfile[2] #accessing nii files
    shutil.copy2(input_dir + verse_file + "/" + moveFile, output_dir + moveFile)
print("Done!")
