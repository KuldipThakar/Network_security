'''The setup.py files is an essential part of the packaging and distributing python projects, it is used by setuptools (or distutils in older python versions) 
to define the configuration of your project, such as its metadeta , dependencies and more '''


from setuptools import find_packages,setup
''' this scans all the folder and whenever there is an init file it consider it as a package  '''

from typing import List


def get_requirements()-> List[str]:
    '''this function will return the list of requirements'''
    requirement_lst: List[str]=[]
    try:
        with open('requirements.txt','r') as file:
            #Read lines from the file
            lines = file.readlines()
            ## process each lines

            for line in lines:
                requirement= line.strip()
                ##this removes the empty lines and spaces -e. also ignore that 
                #why -e? (in reuiqement.txt after all the requirements we need to add .e at the end which needs to be ignore while checking the requirements
                if requirement and requirement != '-e .':
                    requirement_lst.append(requirement)

    except FileNotFoundError:
        raise FileNotFoundError("Requirement.txt not found , ensure that it is there")        
    print("requiement file not found error")
    return requirement_lst
    
setup (
        name ="NetworkSecurity",
        version ="0.0.1.1",
        author = "Kuldip thakar",
        author_email="kuldip.thakar.developer@gmail.com",
        packages=find_packages(),
        install_requires = get_requirements()
           )