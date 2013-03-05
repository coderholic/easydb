from setuptools import setup, find_packages
import os

def read(fname):
    return open(os.path.join(os.path.dirname(__file__), fname)).read()

setup(
    name='easydb',
    version='0.2',
    description='Simple SQLite wrapper to make it easier to manage your database',
    author='Ben Dowling',
    author_email='ben.m.dowling@gmail.com',
    url='https://github.com/coderholic/easydb',
    packages=find_packages(),
    include_package_data=True,
    zip_safe=False,
    long_description=read('readme.md'),
    license = "MIT",
    keywords = "db database sqlite",
)
