from setuptools import setup, find_namespace_packages

setup(name='clean folder',
      version='1',
      description='Program sorts files related to their extensions',
      url='https://github.com/Baskina/python_package',
      author='Baskina',
      author_email='baskina.development@gmail.com',
      license='MIT',
      packages=find_namespace_packages(),
      entry_points={'console_scripts': ['clean-folder = clean_folder.index:main']},
      )