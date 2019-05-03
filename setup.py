
import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
     name='pyawscli',  
     version='0.0.1',
     author="Darshan Raul",
     author_email="cloudforteskills@gmail.com",
     description="A CLI package in python to interact with AWS services",
     long_description=long_description,
   long_description_content_type="text/markdown",
     url="https://github.com/darshan-raul/Python-Package-for-CLI",
      license='MIT',
      packages=['pyawscli'],
      zip_safe=False
 )