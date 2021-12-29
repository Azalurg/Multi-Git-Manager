from setuptools import setup, find_packages
import pathlib

here = pathlib.Path(__file__).parent.resolve()

setup(
    version="2.0.0",
    author="Azalurg",
    name="PythonGitManager",
    packages=find_packages(),
    python_requires=">=3.5, <4",
    install_requires=["datetime", "termcolor"],
)
