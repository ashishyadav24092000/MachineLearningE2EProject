## This file is used for  -> Building our ML application as a package itself (like packages on PypI)

from setuptools import find_packages,setup
from typing import List

HYPHEN_E_DOT = "-e ." # constant string

def get_requirements(file_path:str) -> List[str] :
    """
    This function returns the list of all required libraries
    """
    requirements = []
    with open(file_path) as file_obj:
        requirements = file_obj.readlines()
        requirements = [req.replace("\n","") for req in requirements]

        ## If "-e ." comes in requirements list while READING reading then remove it
        if HYPHEN_E_DOT in requirements:
            requirements.remove(HYPHEN_E_DOT)
    return requirements

setup(
    name="MLE2Eproj",
    version="0.0.1",
    author="ASHISH YADAV",
    author_email="ashishyadav24092000@gmail.com",
    packages=find_packages(),
    install_requires = get_requirements("./requirements.txt")
)



