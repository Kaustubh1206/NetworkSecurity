'''
The setup.py file is an essential part of packaging and distributing Python Projects. 
It is used by setuptools ( or distutils in older Python version ) to defines the configuration of your project, such as its metadata , 
dependencies and more
'''
# this find_package library search for all the folders and the folder which have __init__.py file in it is consider as a package 
from setuptools import find_packages,setup # setup is respobsible for project info
from typing import List

def get_requirements()->List[str]:
    '''
    Thid function will return list of requirements
    '''
    requirement_lst:List[str]=[]
    try:
        with open('requirements.txt','r') as file:
            # Read Lines from the file
            lines=file.readlines()
            # PRocess each line
            for line in lines:
                requirement=line.strip()
                # ignore empty lines and -e .
                if requirement and requirement !='-e .':
                    requirement_lst.append(requirement)
    except FileNotFoundError:
        print("requirements.txt file not found")

    return requirement_lst

setup(
    name="NetworkSecurity",
    version="0.0.1",
    author="Kaustubh",
    author_email="kaustubhgidh06@gmail.com",
    packages=find_packages(),
    install_requires=get_requirements()
)