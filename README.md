# cloner

[![Code style: black](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/python/black)

Lately I have found myself cloning repos to my desktop to work on new features.
I would rather have all of my Github *stuff* in my `~/Documents/Github` folder, but temporarily link the ones I'm currently working on to my desktop.

Cloner is a simple script which does just that.
Rather than using `git clone <repo>`, you use the cloner tool `cloner <repo>` and it automatically clones to the set Github folder and creates a symbolic link to the desktop.

Probably not a useful script for anyone else but me :man_shrugging: but oh well!

```
usage: cloner [-h] [--github <path>] [--desktop <path>] repo

Script to clone repos into my github folder, and also symbolically link to the
desktop.

positional arguments:
  repo              Repository to clone.

optional arguments:
  -h, --help        show this help message and exit
  --github <path>   Path to your Github folder.
  --desktop <path>  Path to your Desktop folder.
```

## Installation

Installation is made easy using pip!

```bash
git clone https://github.com/rhthomas/cloner.git
cd cloner
pip3 install .
```
