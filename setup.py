from setuptools import setup, find_packages

setup(
    name="ltl_parser",  # The name of your package
    version="0.1.0",    # Initial version
    packages=find_packages(where="ltl"),  # Automatically find packages
    include_package_data=True,
    install_requires=[  # Dependencies, if any
        # List dependencies like this:
        # "pyparsing>=3.0.0",
    ],
    tests_require=["pytest"],  # Add pytest as a test dependency
    test_suite="test",  # This will run tests in the `tests` directory
    author="Tiberiu-Andrei Georgescu",
    author_email="tibi.geo@ic.ac.uk",
    description="A simple parser for Linear Temporal Logic (LTL) formulas.",
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    url="https://github.com/TibiIC/py-linear-temporal-logic",  # GitHub link or project URL
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",  # Change the license type if needed
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.6",  # Minimum Python version
)