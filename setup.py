from setuptools import setup, find_packages

# with open('README.rst') as f:
#     readme = f.read()
#
# with open('LICENSE') as f:
#     license = f.read()

with open('requirements.txt', 'r') as f:
    install_requires = f.read().splitlines()

setup(
    name='RaspberryPI NAS',
    version='0.1.0',
    description='RaspberryPI NAS',
    # long_description=readme,
    author='Dzianis Andreyeu',
    author_email='andninbox@gmail.com',
    # url='https://github.com/kennethreitz/samplemod',
    # license=license,
    packages=find_packages(exclude=('tests', 'docs')),
    install_requires=install_requires
)
