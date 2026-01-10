"""
A* pathfinding algorithm implementation.
"""

import pygame
from queue import PriorityQueue
from typing import Callable, Dict
from src.core.node import Node


def manhattan_distance(node1: Node, node2: Node) -> int:
    """
    Calculate Manhattan distance between two nodes.
    
    Args:
        node1: First node
        node2: Second node
        
    Returns:
        Manhattan distance as integer
    """
    x1, y1 = node1.get_position()
    x2, y2 = node2.get_position()
    return abs(x1 - x2) + abs(y1 - y2)


def reconstruct_path(came_from: Dict[Node, Node], current: Node, draw_func: Callable) -> None:
    """
    Reconstruct and visualize the optimal path.
    
    Args:
        came_from: Dictionary mapping each node to its predecessor
        current: Current node (should be the goal)
        draw_func: Function to call for visualization updates
    """
    while current in came_from:
        current = came_from[current]
        current.make_path()
        draw_func()


def astar_search(draw_func: Callable, grid_nodes: list[list[Node]], 
                start: Node, goal: Node) -> bool:
    """
    Execute A* pathfinding algorithm.
    
    Args:
        draw_func: Function to call for visualization updates
        grid_nodes: 2D list of all nodes in the grid
        start: Starting node
        goal: Goal node
        
    Returns:
        True if path found, False otherwise
    """
    count = 0
    open_set = PriorityQueue()
    open_set.put((0, count, start))
    came_from = {}
    
    # Initialize scores
    g_score = {node: float("inf") for row in grid_nodes for node in row}
    g_score[start] = 0
    
    f_score = {node: float("inf") for row in grid_nodes for node in row}
    f_score[start] = manhattan_distance(start, goal)
    
    open_set_hash = {start}  # Track items in priority queue
    
    while not open_set.empty():
        # Handle pygame events to prevent freezing
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                return False
        
        current = open_set.get()[2]  # Get node from priority queue
        open_set_hash.remove(current)
        
        if current == goal:
            reconstruct_path(came_from, goal, draw_func)
            goal.make_goal()  # Ensure goal remains visible
            return True
        
        for neighbor in current.neighbors:
            temp_g_score = g_score[current] + 1  # All edges have weight 1
            
            if temp_g_score < g_score[neighbor]:
                # Found better path to neighbor
                came_from[neighbor] = current
                g_score[neighbor] = temp_g_score
                f_score[neighbor] = temp_g_score + manhattan_distance(neighbor, goal)
                
                if neighbor not in open_set_hash:
                    count += 1
                    open_set.put((f_score[neighbor], count, neighbor))
                    open_set_hash.add(neighbor)
                    neighbor.make_open()
        
        draw_func()
        
        if current != start:
            current.make_visited()
    
    return False  # No path found