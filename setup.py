import setuptools

from testyoke.version import __version__

with open('README.md', 'r') as f:
    long_desc = f.read()

setuptools.setup(
    name='testyoke',
    version=__version__,
    author='trevor grayson',
    author_email='trevor@ipsumllc.com',
    description='Provide insights on the outcomes of software test cases.',
    long_description=long_desc,
    long_description_content_type='text/markdown',
    url='https://github.com/trevorgrayson/testyoke',
    packages=setuptools.find_packages(),
    extras_require={
        'server': ["flask>=1.1.1"],
    },
    classifiers=[
        "Programming Language :: Python :: 3",
    ],
    entry_points = {
        'console_scripts': ['testyoke=testyoke.cli:main'],
    },
    python_requires='>=3.6',
)
