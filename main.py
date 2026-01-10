#!/usr/bin/env python3
"""
Pathfinding Algorithm Visualizer

A Python application that visualizes and compares A* and Dijkstra's pathfinding 
algorithms using Pygame. Select from 4 different maze configurations and see 
how each algorithm performs.

Usage:
    python main.py

Controls:
    - Menu: Press 1-4 to select a maze configuration
    - Visualizer: Press SPACE to start the pathfinding algorithm
    - Close window to proceed to next algorithm or return to menu

Author: Your Name
Course: CS 530 - Artificial Intelligence
"""

import sys
import os

# Add src directory to Python path for imports
sys.path.insert(0, os.path.join(os.path.dirname(__file__), 'src'))

from src.ui.menu import Menu
from src.ui.visualizer import run_both_algorithms


def main():
    """Main application entry point."""
    print("=" * 60)
    print("PATHFINDING ALGORITHM VISUALIZER")
    print("=" * 60)
    print("\\nThis application demonstrates A* and Dijkstra's pathfinding algorithms")
    print("on different maze configurations.\\n")
    print("Instructions:")
    print("1. Select a maze (1-4) from the menu")
    print("2. Press SPACE in each window to start the algorithm")
    print("3. Compare the performance of both algorithms")
    print("4. Close windows to return to menu or exit")
    print("\\n" + "=" * 60 + "\\n")
    
    try:
        while True:
            # Show menu and get user selection
            menu = Menu()
            selected_lab = menu.run()
            
            if selected_lab is None:
                print("Exiting application...")
                break
            
            # Run both algorithms for the selected lab
            run_both_algorithms(selected_lab)
            
            # Ask if user wants to continue
            print("\\nWould you like to try another maze? Close this terminal or press Ctrl+C to exit.")
            print("Otherwise, the menu will appear again...")
            
    except KeyboardInterrupt:
        print("\\n\\nApplication terminated by user.")
    except Exception as e:
        print(f"\\nAn error occurred: {e}")
        print("Please check that all required files are present.")
    finally:
        print("\\nThank you for using the Pathfinding Algorithm Visualizer!")


if __name__ == "__main__":
    main()