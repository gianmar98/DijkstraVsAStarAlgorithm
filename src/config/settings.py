"""
Configuration settings for the pathfinding visualizer.
"""

# Display settings
WINDOW_WIDTH = 800
WINDOW_HEIGHT = 800
GRID_ROWS = 50

# Menu settings
MENU_WIDTH = 800
MENU_HEIGHT = 900
DEFAULT_IMAGE_SIZE = (WINDOW_WIDTH // 2, WINDOW_WIDTH // 2)

# Lab configurations with start and goal positions
LAB_CONFIGS = {
    1: {
        'astar_file': 'data/A1.txt',
        'dijkstra_file': 'data/dijkstra1.txt',
        'start': (30, 30),
        'goal': (1, 1)
    },
    2: {
        'astar_file': 'data/A2.txt',
        'dijkstra_file': 'data/dijkstra2.txt',
        'start': (24, 22),
        'goal': (4, 30)
    },
    3: {
        'astar_file': 'data/A3.txt',
        'dijkstra_file': 'data/dijkstra3.txt',
        'start': (3, 5),
        'goal': (45, 47)
    },
    4: {
        'astar_file': 'data/A4.txt',
        'dijkstra_file': 'data/dijkstra4.txt',
        'start': (42, 26),
        'goal': (6, 44)
    }
}

# Image files
IMAGES = {
    'title': 'assets/title.png',
    'lab1': 'assets/firstLab.png',
    'lab2': 'assets/secondLab.png',
    'lab3': 'assets/thirdLab.png',
    'lab4': 'assets/fourthLab.png'
}