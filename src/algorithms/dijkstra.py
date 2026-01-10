"""
Dijkstra's pathfinding algorithm implementation.
"""

import pygame
from queue import PriorityQueue
from typing import Callable, Dict
from src.core.node import Node


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


def dijkstra_search(draw_func: Callable, grid_nodes: list[list[Node]], 
                   start: Node, goal: Node) -> bool:
    """
    Execute Dijkstra's pathfinding algorithm.
    
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
    
    # Initialize distance scores (g_score in Dijkstra's)
    distance = {node: float("inf") for row in grid_nodes for node in row}
    distance[start] = 0
    
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
            temp_distance = distance[current] + 1  # All edges have weight 1
            
            if temp_distance < distance[neighbor]:
                # Found shorter path to neighbor
                came_from[neighbor] = current
                distance[neighbor] = temp_distance
                
                if neighbor not in open_set_hash:
                    count += 1
                    # Dijkstra uses only distance (no heuristic)
                    open_set.put((distance[neighbor], count, neighbor))
                    open_set_hash.add(neighbor)
                    neighbor.make_open()
        
        draw_func()
        
        if current != start:
            current.make_visited()
    
    return False  # No path found