from __future__ import annotations
from dataclasses import dataclass
from random_gen import RandomGen

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

    @classmethod
    def random(cls):
        return Island(
            RandomGen.random_choice(ISLAND_NAMES),
            RandomGen.random() * 500,
            RandomGen.randint(0, 300),
        )

    def __lt__(self, island2: Island):
        return (self.money/self.marines) < (island2.money/island2.marines)
    def __le__(self, island2: Island):
        return (self.money/self.marines) <= (island2.money/island2.marines)
    def __gt__(self, island2: Island):
        return (self.money/self.marines) > (island2.money/island2.marines)
    def __ge__(self, island2: Island):
        return (self.money/self.marines) >= (island2.money/island2.marines)
    def __eq__(self, island2: Island):
        return (self.money/self.marines) == (island2.money/island2.marines)
    def __ne__(self, island2: Island):
        return (self.money/self.marines) != (island2.money/island2.marines)