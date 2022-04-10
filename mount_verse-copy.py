# azureml-core of version 1.0.72 or higher is required
from azureml.core import Workspace, Dataset, Run
from azureml.data import OutputFileDatasetConfig
import os
import argparse

'''
To Run this script, simply paste the following into the terminal:
python mount_verse.py ~/cloudfiles/code/Users/hbarton7/verse_training_files ~/cloudfiles/code/Users/hbarton7/verse_testing_files ~/cloudfiles/code/Users/hbarton7/verse_validation_files
'''
parser = argparse.ArgumentParser()
parser.add_argument("mount_path_training", type=str, help="The folder location to mount the training dataset too.")
parser.add_argument("mount_path_testing", type=str, help="The folder location to mount the testing dataset too.")
parser.add_argument("mount_path_validation", type=str, help="The folder location to mount the validation dataset too.")
parser.add_argument("--download", action="store_true", default=False, help="Download the data to the desired location instead.")
args = parser.parse_args()

# for the Verse Testing set
subscription_id = '8878c833-bf92-4cf4-a045-b66f5e7cae01'
resource_group = 'RohlingProjects'
workspace_name = 'RohlingML'



workspace = Workspace(subscription_id, resource_group, workspace_name)
names = ['Verse 20 Training', 'Verse 20 Testing', 'Verse 20 Validation']

# mount training set
dataset = Dataset.get_by_name(workspace, name=names[0])
target_path_training = args.mount_path_training
mount_context = dataset.mount(target_path_training)
mount_context.start()

print(os.listdir(target_path_training))
print(target_path_training)

# mount testing set
dataset = Dataset.get_by_name(workspace, name=names[1])
target_path_testing = args.mount_path_testing
mount_context = dataset.mount(target_path_testing)
mount_context.start()

print(os.listdir(target_path_testing))
print(target_path_testing)

# mount vaidation set 
dataset = Dataset.get_by_name(workspace, name=names[2])
target_path_validation = args.mount_path_validation
mount_context = dataset.mount(target_path_validation)
mount_context.start()

print(os.listdir(target_path_validation))
print(target_path_validation)
