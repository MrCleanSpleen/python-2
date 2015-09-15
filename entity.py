"""Entity class (something that is alive- most of the time.)
"""
from stats import HasStats
from inventory import HasIventory

class Entity(HasStats,HasIventory):
    pass
