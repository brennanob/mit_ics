"""
This is a skeleton file that can serve as a starting point for a Python
console script. To run this script uncomment the following lines ii pyproject.toml

[project.scripts]
<name>  = 'package.module:run'

Then run ``pip install .`` (or ``pip install -e .`` for editable mode)
which will install the command inside your current environment.

"""


def count_vowels(s: str):
    vowels = ["a", "e", "i", "o", "u"]
    nvowels = len([x for x in s if x in vowels])
    print("Number of vowels: " + str(nvowels))
