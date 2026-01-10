"""
Node class representing a single cell in the pathfinding grid.
"""

import pygame
from src.ui.colors import COLORS, GREY


class Node:
    """
    Represents a single node/cell in the pathfinding grid.
    
    Attributes:
        row (int): Row position in the grid
        col (int): Column position in the grid
        x (int): X pixel coordinate for drawing
        y (int): Y pixel coordinate for drawing
        color (tuple): RGB color tuple for visualization
        neighbors (list): List of adjacent navigable nodes
        width (int): Width of the node in pixels
        total_rows (int): Total number of rows in the grid
    """
    
    def __init__(self, row: int, col: int, width: int, total_rows: int):
        """
        Initialize a new node.
        
        Args:
            row: Row position in the grid
            col: Column position in the grid
            width: Width of each cell in pixels
            total_rows: Total number of rows in the grid
        """
        self.row = row
        self.col = col
        self.x = row * width
        self.y = col * width
        self.color = GREY
        self.neighbors = []
        self.width = width
        self.total_rows = total_rows

    def get_position(self) -> tuple[int, int]:
        """Get the (row, col) position of this node."""
        return self.row, self.col

    def draw(self, window: pygame.Surface) -> None:
        """Draw this node on the given pygame surface."""
        pygame.draw.rect(window, self.color, (self.x, self.y, self.width, self.width))

    # State checking methods
    def is_barrier(self) -> bool:
        """Check if this node is a barrier."""
        return self.color == COLORS['barrier']

    # State setting methods
    def make_barrier(self) -> None:
        """Mark this node as a barrier."""
        self.color = COLORS['barrier']

    def make_start(self) -> None:
        """Mark this node as the start position."""
        self.color = COLORS['start']

    def make_goal(self) -> None:
        """Mark this node as the goal position."""
        self.color = COLORS['goal']

    def make_path(self) -> None:
        """Mark this node as part of the optimal path."""
        self.color = COLORS['path']

    def make_visited(self) -> None:
        """Mark this node as visited during search."""
        self.color = COLORS['visited']

    def make_open(self) -> None:
        """Mark this node as in the open set (to be explored)."""
        self.color = COLORS['open']

    def update_neighbors(self, grid: list[list['Node']]) -> None:
        """
        Update the list of navigable neighbor nodes.
        
        Args:
            grid: 2D list of all nodes in the grid
        """
        self.neighbors = []
        
        # Check all four directions (up, down, left, right)
        directions = [
            (-1, 0),  # Up
            (1, 0),   # Down
            (0, -1),  # Left
            (0, 1)    # Right
        ]
        
        for dr, dc in directions:
            new_row, new_col = self.row + dr, self.col + dc
            
            # Check bounds and if the neighbor is not a barrier
            if (0 <= new_row < self.total_rows and 
                0 <= new_col < self.total_rows and 
                not grid[new_row][new_col].is_barrier()):
                self.neighbors.append(grid[new_row][new_col])

    def __lt__(self, other: 'Node') -> bool:
        """Less than comparison for priority queue compatibility."""
        return False