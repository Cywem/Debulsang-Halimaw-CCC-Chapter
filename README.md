# Debulsang Halimaw: CCC Chapter

A Pokemon-style battle game built with Python and Pygame, featuring Filipino dialogue and custom characters.

## Project Structure

```
Debulsang Halimaw - CCC Chapter/
├── run_game.py           # Game launcher script
├── README.md             # This file
├── requirements.txt      # Python dependencies
├── .gitignore           # Git ignore patterns
│
├── src/                 # Source code files
│   ├── __init__.py      # Package marker
│   ├── main.py          # Main game entry point
│   └── spritesheet.py   # Sprite animation utilities
│
├── tests/               # Test files
│   └── test_game.py     # Game tests
│
└── docs/                # Documentation
    ├── PROJECT_ORGANIZATION.md
    └── systemWalkthrough.mp4

```

**Note**: The game expects assets (images, audio, fonts) to be in an `assets/` directory with subdirectories `images/`, `audio/`, and `fonts/`. You'll need to place your game assets in these directories before running.

## Features

-   **Pokemon Battle System**: Turn-based combat with type effectiveness
-   **Filipino Language**: Fully localized dialogue in Filipino/Tagalog
-   **Custom Characters**: Unique starter Pokemon (Chespin, Tepig, Piplup)
-   **Animated Sprites**: Smooth sprite animations and battle sequences
-   **Audio Experience**: Background music, sound effects, and dialogue
-   **Visual Effects**: Fade transitions and HP bars

## Installation

1. **Clone or download this repository**

2. **Install dependencies:**

    ```bash
    pip install -r requirements.txt
    ```

    Required packages:

    - pygame
    - opencv-python
    - requests
    - pytest

3. **Run the game:**
    ```bash
    cd src
    python main.py
    ```

## How to Play

1. **Start**: Click the START button after the intro video
2. **Choose Pokemon**: Select your starter Pokemon (Chespin, Tepig, or Piplup)
3. **Battle**: Choose to fight or use potions during your turn
4. **Win**: Defeat your rival's Pokemon to win the battle!

### Controls

-   **Mouse**: Navigate menus and select options
-   **ESC**: Quit game
-   **Y/N**: Play again after game over

## Game Mechanics

-   **Type Effectiveness**: Fire > Grass > Water > Fire
-   **HP System**: Fixed 100 HP for all Pokemon at level 30
-   **Potions**: 3 potions available per battle (+30 HP each)
-   **Move System**: 4 random moves per Pokemon from the PokeAPI
-   **Critical Hits**: 6.25% chance for 1.5x damage
-   **STAB**: Same Type Attack Bonus applies

## Credits

-   **Professor Character**: Sir Visaya
-   **Game Engine**: Pygame
-   **Pokemon Data**: [PokeAPI](https://pokeapi.co/)
-   **Language**: Filipino/Tagalog

## Development

### Running Tests

```bash
pytest tests/
```

### Project Components

-   **main.py**: Core game logic, battle system, and UI
-   **spritesheet.py**: Handles sprite sheet parsing and animation
-   **Pokemon Class**: Manages Pokemon stats, moves, and battle actions
-   **Move Class**: Fetches and stores move data from PokeAPI

## Technical Details

-   **Screen Resolution**: 800x600
-   **FPS**: 60
-   **API**: Real-time Pokemon data from PokeAPI
-   **Video Codec**: OpenCV for intro video playback

## Known Issues

-   Ensure all audio files are present in `assets/audio/`
-   Network connection required for Pokemon sprite loading from API
-   Video intro may be skipped if file is missing

## License

Educational project - Created for Final Requirement of Operating System

## Version

Current Version: 1.0
