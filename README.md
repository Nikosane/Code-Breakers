# Code Breakers 🎮  
**Code Breakers** is a text-based puzzle game where players aim to guess a secret code by cracking clues embedded in randomly generated text snippets. The game progresses through increasingly challenging levels, testing the player's pattern recognition and problem-solving skills.

---

## Features ✨  
- **Dynamic Text Snippets**: Randomly generated text snippets containing hidden patterns.  
- **Player Tools**: Choose tools like key analysis or pattern recognition to decode the clues.  
- **Progressive Difficulty**: Levels become harder as the snippets get more complex.  
- **Scoring System**: Earn points for every successfully cracked code.

---

## Gameplay Instructions 🎲  
1. Start the game by running the `main.py` file.  
2. Each level presents a text snippet with a hidden pattern or code.  
3. Choose one of the available tools to analyze the snippet:  
   - `key_analysis`: Focuses on identifying specific characters or sequences in the snippet.  
   - `pattern_recognition`: Analyzes the overall structure of the snippet.  
4. Use your reasoning to decode the snippet.  
5. Progress to the next level if you succeed; otherwise, try again!  
6. The game ends when you complete all levels or choose to exit.  


---

## Requirements 🛠️  
- Python 3.8 or later  

---

## Installation 🚀  
1. Clone the repository:  
   ```bash
   git clone https://github.com/Nikosane/Code-Breakers.git
   cd code-breakers
   ```
2. Install any dependencies (if required):  
   ```bash
   pip install -r requirements.txt
   ```  
   *(No external libraries are required by default. If you expand the game, update the requirements.)*  
3. Run the game:  
   ```bash
   python main.py
   ```

---

## How It Works 🧩  
1. **Text Snippets**: Snippets are generated based on the level's complexity, which determines the hidden patterns.  
2. **Tools**: Each tool provides a different perspective on decoding the snippet, such as looking for specific keys or recognizing patterns.  
3. **Levels**: Levels are defined in the `levels.json` file and can be customized with new descriptions and complexities.

---

## Customization 🔧  
1. **Add New Levels**: Edit the `data/levels.json` file to add more levels.  
2. **Modify Tools**: Update `tools.py` to include additional tools for analyzing text snippets.  
3. **Patterns**: Add new patterns to `clue_generator.py` to increase variety in snippets.

---

## Future Enhancements 📈  
- **GUI Version**: Transform the text-based game into an interactive graphical experience.  
- **Multiplayer Mode**: Introduce competitive gameplay with leaderboards.  
- **Advanced Tools**: Add machine learning models for pattern detection.  
- **Achievements**: Reward players with badges for milestones.

---

## Contributing 🫱  
Contributions are welcome! If you have ideas for new features or improvements, feel free to fork the repository, make your changes, and create a pull request.

---

## License 📜  
This project is licensed under the [MIT License](LICENSE).

---

## Acknowledgments 🙏  
Thanks to all contributors and testers for making this game a fun experience! 🎉

