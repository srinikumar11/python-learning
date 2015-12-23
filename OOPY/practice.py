class Monster:
    hit_points = 1
    color = "yellow"
    weapon = "sword"
    sound = 'roar'
    
    def battlecry (self):
        return self.sound.upper()
        
        
        
class Store:
  open = 9
  close = 9
  
  def hours(self):
    return "We're open from {open_time} to {close_time}.".format(open_time = self.open, close_time = self.close)
    
    
import random

COLORS = ["red","green","blue","white", "black"]


class Monster:
    # min_hit_points = 1
    # max_hit_points = 1
    # min_experiance = 1
    # max_experiance = 1
    # colors = ["yellow"]
    # weapon = "sword"
    # sound = 'roar'
    
    def battlecry (self):
        return self.sound.upper()
      
    def __init__(self, **kwargs):
      self.hit_points = kwargs.get('hit_points', 1)
      self.color = kwargs.get('color', 'red')
      self.weapon = kwargs.get('weapon', 'sword')
      self.sound = kwargs.get('sound', 'roar')
      
###################
import random

COLORS = ["red","green","blue","white", "black"]

class Monster:
    min_hit_points = 1
    max_hit_points = 1
    min_experiance = 1
    max_experiance = 1
    #colors = ["yellow"]
    weapon = "sword"
    sound = 'roar'
    
    def battlecry (self):
        return self.sound.upper()
      
    def __init__(self, **kwargs):
      self.hit_points = random.randint(self.min_hit_points, self.max_hit_points)
      self.color = random.choice(COLORS)
      self.weapon = self.weapon
      self.sound = self.sound
      
      for key, value in kwargs.items():
        setattr(self, key, value)


# from monster import Monster
# srini = Monster(walker=True, color="purple")
# srini.color
# "purple"
# srini.waler
# True

class Game:
  def __init__(self):
    self.current_score = [0, 0]
  
  def score(self, player):
    self.current_score[player-1] +=  1
    