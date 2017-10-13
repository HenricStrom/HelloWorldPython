from setuptools import setup, find_packages

setup(
    name="HelloWold",
    version="1.0",
    packages=find_packages(),
    entry_points={
        "console_scripts": [
            "make-invoice-predictions = hello_world.main:main"
        ]
    }
)