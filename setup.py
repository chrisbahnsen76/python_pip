from setuptools import setup

setup(
    name='my_pip_package',
    version='0.0.1',
    description='My pip package from my github repo',
    url='git@github.com:chrisbahnsen/python_pip.git',
    author='Christopher Bahnsen',
    author_email='christopher.bahnsen@hitachivantara.com',
    license='unlicense',
    packages=['my_pip_package'],
    zip_safe=False
)
