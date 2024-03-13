from setuptools import find_packages, setup
from typing import List

hyphen_e_dot = '-e .'   # this var is used later in code so we ignore -e . when running this function. having -e . in requirements allows setup to fetch needed packages 
def get_requirements(file_path:str)->List[str]: # so fnc will return a list
    '''
    This fnc will return package requirements
    '''
    requirements = []
    with open(file_path) as file_obj:
        requirements = file_obj.readlines()
        requirements = [req.replace("\n", "") for req in requirements] #will iterate through each line on requirements

        if hyphen_e_dot in requirements:
            requirements.remove(hyphen_e_dot)

    return requirements


setup(name='mlopse2e',
version= '0.0.1',
author= 'Mvuyiso',
author_email='mvuyisogq@gmail.com',
packages=find_packages(),
install_requires = get_requirements('requirements.txt')
)