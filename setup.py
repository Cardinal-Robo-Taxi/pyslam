from setuptools import setup
from setuptools import find_packages


def load(path):
    return open(path, 'r').read()

pyslam_version = '1.4.0'

classifiers = [
    "Development Status :: 5 - Production/Stable",
    "Environment :: Console",
    "Intended Audience :: Science/Research",
    "License :: OSI Approved :: MIT License",
    "Operating System :: OS Independent",
    "Programming Language :: Python",
    "Programming Language :: Python :: 3",
    "Topic :: Scientific/Engineering"
]


if __name__ == "__main__":
    setup(
        name="pyslam",
        version=pyslam_version,
        description="pyslam",
        long_description=load('README.md'),
        long_description_content_type='text/markdown',
        platforms="OS Independent",
        package_data={'pyslam': ['README.md', '*.ini', 'settings/*.yaml']},
        packages=find_packages(exclude=['tests']),
        install_requires=["pandas", "numpy"],
    )
