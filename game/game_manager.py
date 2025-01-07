from game.level_manager import LevelManager
from game.player import Player

class GameManager:
    def __init__(self):
        self.player = Player()
        self.level_manager = LevelManager()

    def start_game(self):
        print("Welcome to Code Breakers!")
        while not self.level_manager.is_game_over():
            level_data = self.level_manager.get_current_level()
            print(f"Level {level_data['level']} - {level_data['description']}")
            print("Snippet:", level_data['snippet'])

            tool = input("Choose a tool (key_analysis/pattern_recognition): ")
            result = self.level_manager.process_tool(tool, level_data['snippet'])
            if result['success']:
                print("Correct! You cracked the code!")
                self.player.increment_score()
                self.level_manager.next_level()
            else:
                print("Incorrect. Try again!")
        print(f"Game Over! Your final score: {self.player.score}")
