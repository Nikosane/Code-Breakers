import json
from game.clue_generator import generate_snippet
from game.tools import analyze_tool

class LevelManager:
    def __init__(self):
        self.current_level = 0
        self.load_levels()
    
    def load_levels(self):
        with open("data/levels.json") as f:
            self.levels = json.load(f)

    def get_current_level(self):
        level = self.levels[self.current_level]
        snippet = generate_snippet(level["complexity"])
        return {
            "level": self.current_level + 1,
            "description": level["description"],
            "snippet": snippet,
        }

    def process_tool(self, tool, snippet):
        return analyze_tool(tool, snippet)

    def next_level(self):
        self.current_level += 1

    def is_game_over(self):
        return self.current_level >= len(self.levels)

