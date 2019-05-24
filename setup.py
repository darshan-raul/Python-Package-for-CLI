
import setuptools

requires = [
    'awscli>=1.16.10,<2.0.0',
    'boto3>=1.9.0,<2.0.0',
    'pyfiglet>=0.7,<0.8',
    'PyInquirer>=1.0.3',
    'progress>=1.5',
    'termcolor>=1.1.0'

    
    
]

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
     name='pyawscli',  
     version='0.1.7',
     author="Darshan Raul",
     author_email="cloudforteskills@gmail.com",
     description="A CLI package in python to interact with AWS services",
     long_description=long_description,
     install_requires=requires,
   long_description_content_type="text/markdown",
     url="https://github.com/darshan-raul/Python-Package-for-CLI",
      license='MIT',
      packages=['pyawscli'],
      zip_safe=False
 )