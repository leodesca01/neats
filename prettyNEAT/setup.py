from setuptools import setup, find_packages

setup(
    name="prettyNEAT",
    version="0.1",
    packages=find_packages(include=["neat_src", "neat_src.*"]),
    # we pin deps in conda already, so no install_requires
)
