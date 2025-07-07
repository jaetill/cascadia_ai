# game/token.py

class Token:
    def __init__(self, animal_type):
        self.animal_type = animal_type  # e.g., "bear", "salmon", "elk", etc.

    def __repr__(self):
        return f"Token({self.animal_type})"
