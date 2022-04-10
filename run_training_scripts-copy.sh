#!/bin/bash
cd ~/cloudfiles/code/Users/rbatra34 # change this to your own user folder
export PYTHONPATH="$PWD/MedicalDataAugmentationTool"
cd MedicalDataAugmentationTool-VerSe/verse2020/training/
python main_spine_localization.py
# python main_vertebrae_localization.py
# python main_vertebrae_segmentation.py
