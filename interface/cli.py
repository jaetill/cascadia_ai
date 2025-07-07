# interface/cli.py
from game.gamestate import GameState
from ai.basic_agent import choose_action

def start_game():
    state = GameState()
    while not state.is_game_over():
        print("\n--- Current Board State ---")
        state.display()

        if state.current_player.is_human:
            action = input("Enter your move (stub for now): ")
            print(f"You entered: {action}")
            # TODO: Validate and apply human move
        else:
            action = choose_action(state)
            print(f"AI chose: {action}")
            state.apply_action(action)

        state.next_turn()

    print("Game Over!")
    state.display_final_score()
