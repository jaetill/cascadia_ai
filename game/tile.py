# game/tile.py

class Tile:
    def __init__(self, id, terrains):
        """
        terrains: a list or set of 2 terrain types (e.g., ["forest", "wetland"])
        """
        self.id = id
        self.terrains = set(terrains)
        self.token = None  # Will hold a Token object later

    def __repr__(self):
        return f"Tile({self.id}, {self.terrains})"
