from setuptools import find_packages,setup
from typing import List

HYPEN_DOT_E = '-e .'

def get_requirements(file_path:str)->List[str]:
    requirements = []
    with open(file_path) as file_obj:
        requirements=file_obj.readlines()
        requirements=[req.replace("\n","") for req in requirements]

        if HYPEN_DOT_E in requirements:
            requirements.remove(HYPEN_DOT_E)

        return requirements


setup(
    name='DiamondPricePrediction',
    version='0.0.1',
    author='Gadhiya Shivani',
    author_email='shivanigadhiya87@gamil.com',
    install_requires = get_requirements('requirement.txt'),
    packages=find_packages()

)