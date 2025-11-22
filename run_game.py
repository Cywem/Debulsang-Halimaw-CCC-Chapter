#!/usr/bin/env python3
"""
Launcher script for Debulsang Halimaw: CCC Chapter
Run this file to start the game.
"""

import sys
from pathlib import Path

# Add src directory to Python path
src_dir = Path(__file__).parent / "src"
sys.path.insert(0, str(src_dir))

# Import and run the game
from main import main_menu

if __name__ == "__main__":
    main_menu()
