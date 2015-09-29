"""A battle engine API (and StoryEng plugin) for Pokemon-like battles"""


class SkilMan():
    uid = 0
    name = ""
    attack = 0
    defense = 0
    exp = 0
    happiness = 0
    hp = 0
    sp_attack = 0
    sp_defense = 0
    speed = 0
    total = 0
    evolves_at = 0
    species = ""
    catch_rate = 0
    growth_rate = 0
    height = 0
    width = 0
    mf_ratio = 0
    abilities = []
    moves = []
    types = []

class Move():
    uid = 0
    name = ""
    description = ""
    category = ""
    learn_type = ""
    power = 0
    accuracy = 0
    pp = 0
    learned_at = ""

class Ability():
    uid = 0
    name = ""
    description = ""

class Type():
    uid = 0
    name = ""
    description = ""

class Controller():
    
    def handle_battle(group1,group2)
        


