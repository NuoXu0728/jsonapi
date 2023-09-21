from setuptools import setup, find_packages

setup(
    name="jsonapi",
    version="0.0.1",
    packages=find_packages(),
    author="Nuo Xu",
    author_email="xu.nuo1@northeastern.edu",
    description="A custom JSON API to handle complex numbers.",
    long_description=open('README.md').read(),
    long_description_content_type="text/markdown",
    url="https://github.com/NuoXu0728/jsonapi",
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
)
