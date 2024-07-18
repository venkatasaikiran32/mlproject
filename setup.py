from setuptools import find_packages,setup

from typing import List

HYPEN_E_DOT='-e .'

def get_requirements(file_path:str)->List[str]:
    '''
    this function will return ther list of requirements
    '''
    requirements=[]
    with open(file_path) as file_obj:
        requirements=file_obj.readlines()
        requirements=[req.replace('\n','') for req in requirements ]


        if HYPEN_E_DOT in requirements:
            requirements.remove(HYPEN_E_DOT)


        





setup(

name='mlproject',
version='0.0.1',
author='sai kiran',
author_email='saikiranmandapati@gmail.com',
package=find_packages(),
#but there is better way insatll_requires=['pandas','numpy','seaborn']
install_requires=get_requirements('requirements.txt')


 )