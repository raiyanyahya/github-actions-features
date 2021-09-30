from setuptools import find_packages, setup

setup(
    name="wxyz",
    version="1.0.0",
    description="a test cli project ",
    packages=find_packages(),
    install_requires=["click", "pytest"],
    extras_require={"test": ["coverage", "pytest", "pytest-cov"]},
    entry_points={"console_scripts": ["wxyz=wxyz.cli:cli"]},
    tests_require=["mock >= 2.0.0"],
)
