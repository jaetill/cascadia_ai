# game/gamestate.py
from game.player import Player
from game.draft import generate_draft_row

class GameState:
    def __init__(self):
        self.players = [Player("Human", is_human=True), Player("AI_Bot")]
        self.turn = 0
        self.draft_row = generate_draft_row()

    @property
    def current_player(self):
        return self.players[self.turn % len(self.players)]

    def is_game_over(self):
        # Placeholder: End after 5 turns for testing
        return self.turn >= 10

    def next_turn(self):
        self.turn += 1
        self.draft_row = generate_draft_row()

    def apply_action(self, action):
        # Placeholder: Log the action (real logic comes later)
        print(f"Applying action: {action}")

    def display(self):
        print(f"Turn {self.turn} - {self.current_player.name}'s move")

    def display_final_score(self):
        print("Final scoring not yet implemented.")
