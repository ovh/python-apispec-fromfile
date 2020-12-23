from setuptools import find_packages
from setuptools import setup


with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setup(
    name="APISpec-fromfile",
    version="1.0.1",
    author="OVHCloud",
    author_email="opensource@ovhcloud.com",
    description="APISpec plugin to import OpenAPI specifications from a file instead of putting YAML into docstrings",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/ovh/python-apispec-fromfile",
    package_dir={"": "src"},
    packages=find_packages(where="src"),
    classifiers=[
        "Environment :: Plugins",
        "Environment :: Web Environment",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: Apache Software License",
        "Programming Language :: Python",
        "Topic :: Documentation",
        "Topic :: Internet :: WWW/HTTP",
        "Topic :: Software Development :: Libraries :: Python Modules",
    ],
    keywords="openapi apispec",
    install_requires=[
        "apispec[yaml]",
    ],
    python_requires=">=3.5",
    tests_require=["pytest"],
    test_suite="tests",
)
