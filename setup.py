from setuptools import setup,find_packages
from typing import List
#Declaring variables for setup functions
PROJECT_NAME="breast-cancer-prediction"
VERSION="0.0.3"
AUTHOR="Aswin nath"
DESRCIPTION="This is a End to End machine learning prediction system . It uses a CI/CD pipeline that automatically download data from a remote source and validate , transform , train model , evaluate and push that model for production."

REQUIREMENT_FILE_NAME="requirements.txt"


def get_requirements_list()->List[str]:
    """
   
    Description: This function is going to return list of requirement 
    mention in requirements.txt file

    return This function is going to return a list which contain name 
    of libraries mentioned in requirements.txt file
    """
    with open(REQUIREMENT_FILE_NAME) as requirement_file:
        return requirement_file.readlines().remove("-e .")


setup(
name=PROJECT_NAME,
version=VERSION,
author=AUTHOR,
description=DESRCIPTION,
packages=find_packages(), 
install_requires=get_requirements_list()
)

