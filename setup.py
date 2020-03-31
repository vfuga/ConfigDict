from setuptools import setup, find_packages
from os import path

# io.open is needed for projects that support Python 2.7
# It ensures open() defaults to text mode with universal newlines,
# and accepts an argument to specify the text encoding
# Python 3 only projects can skip this import
from io import open

here = path.abspath(path.dirname(__file__))

# Get the long description from the README file
with open(path.join(here, 'README.md'), encoding='utf-8') as f:
    long_description = f.read()

# Arguments marked as "Required" below must be included for upload to PyPI.
# Fields marked as "Optional" may be commented out.

setup(
    name='ConfigDict',
    version='0.0.1',
    description='A Hierarchical Dictionary',  # Optional
    long_description=long_description,

    # Denotes that our long_description is in Markdown; valid values are
    # text/plain, text/x-rst, and text/markdown
    long_description_content_type='text/markdown',
    url='https://github.com/vfuga/ConfigDict',
    author='Vyacheslav Fuga',
    author_email='vyacheslav.fuga@gmail.com',

    # Classifiers help users find your project by categorizing it.
    #
    # For a list of valid classifiers, see https://pypi.org/classifiers/
    classifiers=[  # Optional
        # How mature is this project? Common values are
        #   3 - Alpha
        #   4 - Beta
        #   5 - Production/Stable
        #'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers, Data Science, Parameters Tool, Configuration Tool, Pipeline configuration',
        'Topic :: Software Development :: Build Tools',
        # Pick your license as you wish
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3',
    ],

    keywords='Python Pipeline configuration',
    #package_dir={'': 'ConfigDict'},
    #packages=find_packages(where='ConfigDict'),
    packages=find_packages(),
    python_requires='>=3.1'
)
