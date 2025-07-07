# game/draft.py

from game.tile import Tile
from game.token import Token
import random

TERRAIN_TYPES = ["forest", "wetland", "mountain", "prairie", "river"]
ANIMAL_TYPES = ["bear", "elk", "hawk", "salmon", "fox"]

def generate_tile(id):
    terrains = random.sample(TERRAIN_TYPES, 2)
    return Tile(id=id, terrains=terrains)

def generate_token():
    return Token(animal_type=random.choice(ANIMAL_TYPES))

def generate_draft_row():
    return [(generate_tile(i), generate_token()) for i in range(4)]
