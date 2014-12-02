__author__ = 'harishrohini'
from distutils.core import setup

setup(name='EECS645',
      version='1.0',
      description='MIPS-64 pipeline Implementation',
      author='Harish Rohini',
      author_email='harishrohini@ku.edu',
      url='https://github.com/HarishRohini/eecs645',
      packages=['instructionstages', 'instructiontypes'],
      py_modules = ['Clock', 'FPOperations', 'Instructions', 'main', 'Memory', 'ReadContents', 'Registers', 'Writer']
     )