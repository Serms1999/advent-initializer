from setuptools import setup, find_packages

with open('README.md', mode='r') as file:
    long_description = file.read()

with open('COPYING', mode='r') as file:
    license = file.read()

with open('requirements.txt', mode='r') as file:
    required = file.read().splitlines()

setup(
    name='adventofcode-initializer',
    version='1.0.1',
    license=license,
    author='Sergio Marín Sánchez',
    author_email='serms1999@gmail.com',
    description='Download Advent of Code problems as markdown files and also its inputs',
    long_description_content_type='text/markdown',
    long_description=long_description,
    url='https://github.com/Serms1999/advent-initializer',
    packages=find_packages(),
    python_requires='>=3.6',
    install_requires=required,
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: GNU General Public License v3 (GPLv3)',
        'Operating System :: OS Independent'
    ],
    entry_points={
        'console_scripts': {'adventofcode-initializer = src.__main__:main'}
    }
)
