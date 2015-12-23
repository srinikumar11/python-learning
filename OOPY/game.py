from charater import Character
from monster import Dragon
from monster import Troll
from monster import Gobblin


class Game:
    def setup(self):
        self.player = Character()
        self.monsters = [
            Dragon(),
            Troll(),
            Gobblin()
        ]
        self.get_next_monster()
    
    def get_next_monster(self):
        try:
            return self.monster.pop(0)
        except IndexError:
            return None
        
            
    def monster_turn(self):
        #Check to see if the monster attacks.
        #If so tell the player.
            #Check if the player wants to dodge,
            #if so see if the dodge is successful.
                #If it is, move on.
            #If it's not, move one player hit point [NOISE].
            #If the monster isn't attacking.Tell that to the player too.
    
    def player_turn(self):
        