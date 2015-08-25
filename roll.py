"""A simple dice rolling module
"""

import random

def roll(howmany=1,sides=6):
    """Returns the result from rolling `howmany of `sides`-sided dice"""
    total = 0
    for count in range(howmany):
        total += random.randint(1,sides)
        return total

if __name__ == '__main__':
    roll()
