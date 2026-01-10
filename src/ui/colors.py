"""
Color definitions for the pathfinding visualizer.
"""

# RGB color constants
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
YELLOW = (255, 255, 0)
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
PURPLE = (128, 0, 128)
ORANGE = (255, 165, 0)
GREY = (128, 128, 128)
TURQUOISE = (64, 224, 208)

# Semantic color mapping
COLORS = {
    'barrier': BLACK,
    'start': ORANGE,
    'goal': GREEN,
    'path': GREEN,
    'visited': BLUE,
    'open': TURQUOISE,
    'empty': GREY,
    'background': BLACK
}