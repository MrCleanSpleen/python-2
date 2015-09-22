"""Pokemon Class/Interface"""

class Pokemon():
    level = 1
    xp = 0
    height = 0
    weight = 0
    weight = 0
    speed = 0
    hp = 0
    attack = 0
    special attack = 0
    defense = 0
    special defense = 0
    type1 = ""
    type2 = ""
    usable_moves = [Inner Focus]
    moves = []
    
    def choose_move(self.move):
        if move in usable_moves:
            self.move = move

    def attack(self,target):
        """Resolve each attack exactly as done in game"""
        A = target.level
        B = self.attack
        D = target.defense
        if self.move.is_special:
            B = self.special_attack
            D = self.special_defense
        C = self.move.power
        X = 1
        if self.move.type in [self.type1,self.type2]
            X = 1.5
        # TODO resolve Y


       # ((2A/5+2)*B*C)/D/50)*X)*Y) *Z/255

class Zubat(Pokemon):
    level = 21
    xp = 0
    height = 0.79
    weight = 7.5
    speed = 55
    hp = 40
    attack = 45
    special_attack = 30
    defense = 35
    special_defense = 40
    type1 = "Poison"
    type2 = "Flying"
    usable_moves = []
    moves = []

    
