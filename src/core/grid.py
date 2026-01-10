"""
Grid management for the pathfinding visualizer.
"""

import pygame
from typing import List
from src.core.node import Node
from src.ui.colors import COLORS, GREY


class Grid:
    """
    Manages the 2D grid of nodes for pathfinding visualization.
    """
    
    def __init__(self, rows: int, width: int):
        """
        Initialize a new grid.
        
        Args:
            rows: Number of rows and columns in the grid
            width: Total width of the display window in pixels
        """
        self.rows = rows
        self.width = width
        self.gap = width // rows  # Width of each cell
        self.nodes = self._create_grid()
    
    def _create_grid(self) -> List[List[Node]]:
        """Create a 2D grid of Node objects."""
        grid = []
        for i in range(self.rows):
            grid.append([])
            for j in range(self.rows):
                node = Node(i, j, self.gap, self.rows)
                grid[i].append(node)
        return grid
    
    def get_node(self, row: int, col: int) -> Node:
        """Get the node at the specified position."""
        return self.nodes[row][col]
    
    def load_barriers_from_file(self, filename: str) -> None:
        """
        Load barrier positions from a text file.
        
        Args:
            filename: Path to the file containing barrier coordinates
        """
        try:
            with open(filename, 'r') as file:
                for line in file:
                    if line.strip():  # Skip empty lines
                        coords = line.strip().split(',')
                        if len(coords) >= 2:
                            row, col = int(coords[0]), int(coords[1])
                            if 0 <= row < self.rows and 0 <= col < self.rows:
                                self.nodes[row][col].make_barrier()
        except FileNotFoundError:
            print(f"Warning: Could not find barrier file {filename}")
        except ValueError as e:
            print(f"Warning: Error parsing barrier file {filename}: {e}")
    
    def set_start_and_goal(self, start_pos: tuple[int, int], goal_pos: tuple[int, int]) -> tuple[Node, Node]:
        """
        Set the start and goal positions on the grid.
        
        Args:
            start_pos: (row, col) tuple for start position
            goal_pos: (row, col) tuple for goal position
            
        Returns:
            Tuple of (start_node, goal_node)
        """
        start_node = self.nodes[start_pos[0]][start_pos[1]]
        goal_node = self.nodes[goal_pos[0]][goal_pos[1]]
        
        start_node.make_start()
        goal_node.make_goal()
        
        return start_node, goal_node
    
    def update_all_neighbors(self) -> None:
        """Update neighbor lists for all nodes in the grid."""
        for row in self.nodes:
            for node in row:
                node.update_neighbors(self.nodes)
    
    def draw(self, window: pygame.Surface) -> None:
        """
        Draw the entire grid on the pygame window.
        
        Args:
            window: Pygame surface to draw on
        """
        # Fill background
        window.fill(GREY)
        
        # Draw all nodes
        for row in self.nodes:
            for node in row:
                node.draw(window)
        
        # Draw grid lines
        self._draw_grid_lines(window)
        
        # Update display
        pygame.display.update()
    
    def _draw_grid_lines(self, window: pygame.Surface) -> None:
        """Draw the grid lines on the window."""
        for i in range(self.rows):
            # Horizontal lines
            pygame.draw.line(window, COLORS['barrier'], 
                           (0, i * self.gap), (self.width, i * self.gap))
            # Vertical lines
            pygame.draw.line(window, COLORS['barrier'], 
                           (i * self.gap, 0), (i * self.gap, self.width))