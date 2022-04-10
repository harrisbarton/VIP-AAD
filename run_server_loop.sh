#!/bin/bash
# comment these three lines below after you run this once on your new compute node
python mount_verse.py ~/cloudfiles/code/Users/hbarton7/verse_training_files ~/cloudfiles/code/Users/hbarton7/verse_testing_files ~/cloudfiles/code/Users/hbarton7/verse_validation_files 
cd MedicalDataAugmentationTool-VerSe/VerSe2020
# pip install -r requirements_current.txt
cd ~/cloudfiles/code/Users/hbarton7 # change this to your user folder
export PYTHONPATH="$PWD/MedicalDataAugmentationTool"
cd MedicalDataAugmentationTool-VerSe/verse2020/training/
python server_dataset_loop.py
