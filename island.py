from __future__ import annotations
from dataclasses import dataclass
from random_gen import RandomGen
import math

# Islands can have names other than this. This is just used for random generation.
ISLAND_NAMES = [
    "Dawn Island",
    "Shimotsuki Village",
    "Gecko Islands",
    "Baratie",
    "Conomi Islands",
    "Drum Island",
    "Water 7"
    "Ohara",
    "Thriller Bark",
    "Fish-Man Island",
    "Zou",
    "Wano Country",
    "Arabasta Kingdom",
    # 13 🌞 🏃‍♀️
    "Loguetown",
    "Cactus Island",
    "Little Garden",
    "Jaya",
    "Skypeia",
    "Long Ring Long Land",
    "Enies Lobby",
    "Sabaody Archipelago",
    "Impel Down",
    "Marineford",
    "Punk Hazard",
    "Dressrosa",
    "Whole Cake Island",
]

@dataclass
class Island:

    name: str
    money: float
    marines: int
    crew: int = 0

    @classmethod
    def random(cls):
        return Island(
            RandomGen.random_choice(ISLAND_NAMES),
            RandomGen.random() * 500,
            RandomGen.randint(0, 300),
            0
        )

    def __lt__(self, island2: Island):
        if self.marines == 0 and island2.marines == 0:
            return max((2*(self.crew-self.marines)), 0)+(min((self.money*self.crew),self.money)) < max((2*(island2.crew-island2.marines)), 0)+(min((island2.money*island2.crew), island2.money))
        elif island2.marines == 0:
            return max((2*(self.crew-self.marines)), 0)+(min((self.money*self.crew)/self.marines,self.money)) < max((2*(island2.crew-island2.marines)), 0)+(min((island2.money*island2.crew), island2.money))
        elif self.marines == 0:
            return max((2*(self.crew-self.marines)), 0)+(min((self.money*self.crew),self.money)) < max((2*(island2.crew-island2.marines)), 0)+(min((island2.money*island2.crew)/island2.marines, island2.money))
        else:
            return max((2*(self.crew-self.marines)), 0)+(min((self.money*self.crew)/self.marines,self.money)) < max((2*(island2.crew-island2.marines)), 0)+(min((island2.money*island2.crew)/island2.marines, island2.money))
        

    def __le__(self, island2: Island):
        if self.marines == 0 and island2.marines == 0:
            return max((2*(self.crew-self.marines)), 0)+(min((self.money*self.crew),self.money)) <= max((2*(island2.crew-island2.marines)), 0)+(min((island2.money*island2.crew), island2.money))
        elif island2.marines == 0:
            return max((2*(self.crew-self.marines)), 0)+(min((self.money*self.crew)/self.marines,self.money)) <= max((2*(island2.crew-island2.marines)), 0)+(min((island2.money*island2.crew), island2.money))
        elif self.marines == 0:
            return max((2*(self.crew-self.marines)), 0)+(min((self.money*self.crew),self.money)) <= max((2*(island2.crew-island2.marines)), 0)+(min((island2.money*island2.crew)/island2.marines, island2.money))
        else:
            return max((2*(self.crew-self.marines)), 0)+(min((self.money*self.crew)/self.marines,self.money)) <= max((2*(island2.crew-island2.marines)), 0)+(min((island2.money*island2.crew)/island2.marines, island2.money))
 
 
    def __gt__(self, island2: Island):
        if self.marines == 0 and island2.marines == 0:
            return max((2*(self.crew-self.marines)), 0)+(min((self.money*self.crew),self.money)) > max((2*(island2.crew-island2.marines)), 0)+(min((island2.money*island2.crew), island2.money))
        elif island2.marines == 0:
            return max((2*(self.crew-self.marines)), 0)+(min((self.money*self.crew)/self.marines,self.money)) > max((2*(island2.crew-island2.marines)), 0)+(min((island2.money*island2.crew), island2.money))
        elif self.marines == 0:
            return max((2*(self.crew-self.marines)), 0)+(min((self.money*self.crew),self.money)) > max((2*(island2.crew-island2.marines)), 0)+(min((island2.money*island2.crew)/island2.marines, island2.money))
        else:
            return max((2*(self.crew-self.marines)), 0)+(min((self.money*self.crew)/self.marines,self.money)) > max((2*(island2.crew-island2.marines)), 0)+(min((island2.money*island2.crew)/island2.marines, island2.money))
   
   
    def __ge__(self, island2: Island):
        if self.marines == 0 and island2.marines == 0:
            return max((2*(self.crew-self.marines)), 0)+(min((self.money*self.crew),self.money)) >= max((2*(island2.crew-island2.marines)), 0)+(min((island2.money*island2.crew), island2.money))
        elif island2.marines == 0:
            return max((2*(self.crew-self.marines)), 0)+(min((self.money*self.crew)/self.marines,self.money)) >= max((2*(island2.crew-island2.marines)), 0)+(min((island2.money*island2.crew), island2.money))
        elif self.marines == 0:
            return max((2*(self.crew-self.marines)), 0)+(min((self.money*self.crew),self.money)) >= max((2*(island2.crew-island2.marines)), 0)+(min((island2.money*island2.crew)/island2.marines, island2.money))
        else:
            return max((2*(self.crew-self.marines)), 0)+(min((self.money*self.crew)/self.marines,self.money)) >= max((2*(island2.crew-island2.marines)), 0)+(min((island2.money*island2.crew)/island2.marines, island2.money))
  
  
    def __eq__(self, island2: Island):
        if self.marines == 0 and island2.marines == 0:
            return max((2*(self.crew-self.marines)), 0)+(min((self.money*self.crew),self.money)) == max((2*(island2.crew-island2.marines)), 0)+(min((island2.money*island2.crew), island2.money))
        elif island2.marines == 0:
            return max((2*(self.crew-self.marines)), 0)+(min((self.money*self.crew)/self.marines,self.money)) == max((2*(island2.crew-island2.marines)), 0)+(min((island2.money*island2.crew), island2.money))
        elif self.marines == 0:
            return max((2*(self.crew-self.marines)), 0)+(min((self.money*self.crew),self.money)) == max((2*(island2.crew-island2.marines)), 0)+(min((island2.money*island2.crew)/island2.marines, island2.money))
        else:
            return max((2*(self.crew-self.marines)), 0)+(min((self.money*self.crew)/self.marines,self.money)) == max((2*(island2.crew-island2.marines)), 0)+(min((island2.money*island2.crew)/island2.marines, island2.money))
  
  
    def __ne__(self, island2: Island):
        if self.marines == 0 and island2.marines == 0:
            return max((2*(self.crew-self.marines)), 0)+(min((self.money*self.crew),self.money)) != max((2*(island2.crew-island2.marines)), 0)+(min((island2.money*island2.crew), island2.money))
        elif island2.marines == 0:
            return max((2*(self.crew-self.marines)), 0)+(min((self.money*self.crew)/self.marines,self.money)) != max((2*(island2.crew-island2.marines)), 0)+(min((island2.money*island2.crew), island2.money))
        elif self.marines == 0:
            return max((2*(self.crew-self.marines)), 0)+(min((self.money*self.crew),self.money)) != max((2*(island2.crew-island2.marines)), 0)+(min((island2.money*island2.crew)/island2.marines, island2.money))
        else:
            return max((2*(self.crew-self.marines)), 0)+(min((self.money*self.crew)/self.marines,self.money)) != max((2*(island2.crew-island2.marines)), 0)+(min((island2.money*island2.crew)/island2.marines, island2.money))