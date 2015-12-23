import random
from combat import Combat

COLORS = ["red","green","blue","white", "black"]


class Monster(Combat):
    min_hit_points = 1
    max_hit_points = 1
    min_experiance = 1
    max_experiance = 1
    #colors = ["yellow"]
    weapon = "sword"
    sound = 'roar'
    
    def __str__(self):
        return '{} {}, HP: {}, XP: {}'.format(
            self.color.title(),
            self.__class__.__name__,
            self.hit_points,
            self.experiance
        )
        
    def battlecry (self):
        return self.sound.upper()
      
    def __init__(self, **kwargs):
      self.hit_points = random.randint(self.min_hit_points, self.max_hit_points)
      self.color = random.choice(COLORS)
      self.weapon = self.weapon
      self.sound = self.sound
      self.experiance = random.randint(self.min_experiance, self.max_experiance)
      
      for key, value in kwargs.items():
        setattr(self, key, value)


class Gobblin(Monster):
    max_hit_points = 3
    max_experiance = 2
    sound = "squeak"
    
    
class Troll(Monster):
    min_hit_points = 4
    max_hit_points = 6
    min_experiance = 4
    max_experiance = 10
    weapon = "sword"
    sound = 'roar'
    
class Dragon(Monster):
    min_hit_points = 4
    max_hit_points = 6
    min_experiance = 4
    max_experiance = 10
    weapon = "sword"
    sound = 'roar'
    
