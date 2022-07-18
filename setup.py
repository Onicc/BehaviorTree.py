import setuptools
from pathlib import Path
import sys

PACKAGE_NAME='behaviortree'
import shutil, os
shutil.copy('README.md', PACKAGE_NAME + '/README.md')

def readme():
    with open("README.md", "r") as fh:
        long_description = fh.read()
        return long_description

v = Path(PACKAGE_NAME + "/version").open(encoding = "utf-8").read().splitlines()


required_packages=[
    'numpy',
    'lxml'
]

setuptools.setup(
    name='behaviortree',
    version=v[0].strip(),
    author="Xinchen Cai",
    author_email="xinchen.cai@hotmail.com",
    description="Python-based behavior tree implementation.",
    long_description=readme(),
    long_description_content_type="text/markdown",
    url="https://github.com/Onicc/BehaviorTree.py",
    packages=setuptools.find_packages(),
    install_requires=required_packages,
    classifiers=[
        "Programming Language :: Python :: 3",
        "Topic :: Scientific/Engineering",
        "Topic :: Scientific/Engineering :: Artificial Intelligence",
        "License :: OSI Approved :: MIT License",
        ],
    keywords='Behavior Tree, behaviortree',
    include_package_data=True,
    package_data={'behaviortree': ['README.md','version']},
    zip_safe=False
)

os.remove('behaviortree/README.md')
