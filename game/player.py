# game/player.py
class Player:
    def __init__(self, name, is_human=False):
        self.name = name
        self.is_human = is_human
        self.board = []  # Stub for now
