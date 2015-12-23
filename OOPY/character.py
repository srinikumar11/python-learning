import random
from combat import Combat


class Character(Combat):
    attack_limit = 10
    experiance = 0
    base_hit_points = 10
    
    def attack(self):
        roll = random.randint(1, self.attack_limit)
        if self.weapon == "sword":
            roll += 1
        elif self.weapon == "axe":
            roll += 2
        
        return roll > 4
        
    def get_weapon(self):
        weapon = input("Weapons ([S]word, [G]un, [A]xe) : ").lower()
        if weapon in "sga":
            if weapon == "s":
                return "sword"
            elif weapon == "g":
                return "gun"
            else:
                return "axe"
        else:
            self.get_weapon()
        
        
    def __init__(self):
        self.name = input("Name : ")
        self.weapon = self.get_weapon()
        self.hit_points = self.base_hit_points
    
    def __str__(self):
        return "{}, HP: {}, XP: {}".format(self.name, self.hit_points, self.experiance)
    
    def rest(self):
        if self.hit_points < self.base_hit_points:
            self.hit_points += 1
    
    def leveled_up(self):
        return self.experiance >= 5