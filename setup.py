from setuptools import find_packages, setup

with open('README.md', 'r') as f:
    long_description = f.read()

setup(
    name='kenbers-calculator',
    version='0.1.0',
    author='Ed. Kenbers',
    author_email='git@kenbers.com',
    description='A simple calculator',
    long_description=long_description,
    long_description_content_type='text/markdown',
    url='https://github.com/EdKenbers/kenbers-calculator',
    packages=find_packages('src')
)