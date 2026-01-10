"""
Main visualizer for pathfinding algorithms.
"""

import pygame
import time
from typing import Optional
from src.core.grid import Grid
from src.core.node import Node
from src.algorithms.astar import astar_search
from src.algorithms.dijkstra import dijkstra_search
from src.config.settings import WINDOW_WIDTH, WINDOW_HEIGHT, GRID_ROWS, LAB_CONFIGS


class PathfindingVisualizer:
    """
    Main visualizer class for pathfinding algorithms.
    """
    
    def __init__(self, lab_number: int, algorithm: str = "astar"):
        """
        Initialize the visualizer.
        
        Args:
            lab_number: Lab configuration number (1-4)
            algorithm: Algorithm to use ("astar" or "dijkstra")
        """
        self.lab_number = lab_number
        self.algorithm = algorithm
        self.lab_config = LAB_CONFIGS[lab_number]
        
        # Initialize pygame
        pygame.init()
        self.window = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
        
        # Set window title based on algorithm
        if algorithm == 'astar':
            title = "A* Path Finding Algorithm"
        else:
            title = "Dijkstra's Path Finding Algorithm"
        pygame.display.set_caption(title)
        
        # Initialize grid
        self.grid = Grid(GRID_ROWS, WINDOW_WIDTH)
        self.start_node: Optional[Node] = None
        self.goal_node: Optional[Node] = None
        
        # State
        self.running = True
        self.algorithm_started = False
        
        # Setup the maze
        self._setup_maze()
    
    def _setup_maze(self) -> None:
        """Setup the maze with barriers and start/goal positions."""
        # Load barriers from file
        barrier_file = (self.lab_config['astar_file'] if self.algorithm == 'astar' 
                       else self.lab_config['dijkstra_file'])
        self.grid.load_barriers_from_file(barrier_file)
        
        # Set start and goal positions
        start_pos = self.lab_config['start']
        goal_pos = self.lab_config['goal']
        self.start_node, self.goal_node = self.grid.set_start_and_goal(start_pos, goal_pos)
    
    def handle_events(self) -> None:
        """Handle pygame events."""
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False
            
            if not self.algorithm_started and event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE and self.start_node and self.goal_node:
                    self._run_algorithm()
    
    def _run_algorithm(self) -> None:
        """Execute the selected pathfinding algorithm."""
        self.algorithm_started = True
        
        # Update all neighbor relationships
        self.grid.update_all_neighbors()
        
        # Create draw function for algorithm visualization
        draw_func = lambda: self.grid.draw(self.window)
        
        # Run the algorithm and measure time
        start_time = time.time()
        
        if self.algorithm == "astar":
            success = astar_search(draw_func, self.grid.nodes, self.start_node, self.goal_node)
        else:  # dijkstra
            success = dijkstra_search(draw_func, self.grid.nodes, self.start_node, self.goal_node)
        
        end_time = time.time()
        
        # Print results
        algorithm_name = "A*" if self.algorithm == "astar" else "Dijkstra's"
        if success:
            print(f"{algorithm_name} algorithm completed successfully!")
            print(f"Total time: {end_time - start_time:.4f} seconds")
        else:
            print(f"{algorithm_name} algorithm: No path found!")
    
    def run(self) -> None:
        """Run the main visualization loop."""
        clock = pygame.time.Clock()
        
        while self.running:
            self.handle_events()
            self.grid.draw(self.window)
            clock.tick(60)  # 60 FPS
        
        pygame.quit()


def run_both_algorithms(lab_number: int) -> None:
    """
    Run both A* and Dijkstra's algorithms for comparison.
    
    Args:
        lab_number: Lab configuration number (1-4)
    """
    print(f"\\n=== Running Lab {lab_number} ===")
    
    # Run A* algorithm
    print("\\nStarting A* Algorithm...")
    print("Press SPACE to start the algorithm, or close window to continue to Dijkstra's")
    astar_viz = PathfindingVisualizer(lab_number, "astar")
    astar_viz.run()
    
    # Run Dijkstra's algorithm
    print("\\nStarting Dijkstra's Algorithm...")
    print("Press SPACE to start the algorithm, or close window to finish")
    dijkstra_viz = PathfindingVisualizer(lab_number, "dijkstra")
    dijkstra_viz.run()
    
    print(f"\\n=== Lab {lab_number} Complete ===\\n")