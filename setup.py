from setuptools import find_packages,setup
from typing import List

HYPEN_E_DOT = '-e .'

def getRequirements(file_path:str):
    '''
    this function return the list of requirement
    '''
    requirement = []
    with open(file_path) as file_obj:
        requirement = file_obj.readlines()
        requirement = [req.replace('\n','')for req in requirement]

        if HYPEN_E_DOT in requirement:
            requirement.remove(HYPEN_E_DOT)
    return requirement    



setup(name="mlproject" , version='0.0.1',
      author="saurabh",
      author_email='saurabhvns24@gmail.com',
      packages=find_packages(),
      install_requires=getRequirements('requirement.txt')
      )