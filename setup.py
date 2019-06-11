from setuptools import setup, find_packages

setup(
    name="Cloner",
    version="0.2",
    packages=find_packages(),
    author="Rhys Thomas",
    author_email="rhys97@me.com",
    description="Clone and link script",
    entry_points={
        "console_scripts": ["cloner=cloner.cli:main"]  # command=package.module:function
    },
)
