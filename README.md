# Pathfinding Algorithm Visualizer

A Python application that visualizes and compares A* and Dijkstra's pathfinding algorithms using Pygame. This project demonstrates the differences between informed and uninformed search algorithms through interactive maze solving.

## 🎯 Features

- **Interactive Visualization**: Watch algorithms explore the maze in real-time
- **Algorithm Comparison**: Compare A* (informed) vs Dijkstra's (uninformed) algorithms
- **Multiple Maze Configurations**: 4 different maze layouts to test
- **Performance Metrics**: Execution time measurement for each algorithm
- **Clean Architecture**: Well-structured, modular codebase suitable for educational purposes

## 🚀 Quick Start

### Prerequisites

- Python 3.8 or higher
- pip (Python package installer)

### Installation

1. **Clone the repository**
   ```bash
   git clone https://github.com/gianmar98/DijkstraVsAStarAlgorithm.git
   cd pathfinding-visualizer
   ```

2. **Create and activate virtual environment**
   ```bash
   python3 -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

4. **Run the application**
   ```bash
   python main.py
   ```

## 🎮 How to Use

1. **Select a Maze**: Press keys 1-4 to choose from different maze configurations
2. **Start Algorithm**: Press SPACE to begin the pathfinding visualization
3. **Observe**: Watch as the algorithm explores the maze:
   - 🟠 **Orange**: Start position
   - 🟢 **Green**: Goal position  
   - 🔵 **Blue**: Visited nodes
   - 🟦 **Turquoise**: Nodes in exploration queue
   - ⬛ **Black**: Barriers/walls
   - 🟢 **Green path**: Final optimal route

4. **Compare**: After A* completes, Dijkstra's algorithm will run on the same maze
5. **Analyze**: Check the terminal for execution time comparisons

## 📊 Algorithm Comparison

| Algorithm | Type | Heuristic | Optimality | Time Complexity |
|-----------|------|-----------|------------|-----------------|
| **A*** | Informed Search | Manhattan Distance | Optimal* | O(b^d) |
| **Dijkstra's** | Uninformed Search | None | Optimal | O(V²) |

*Optimal when heuristic is admissible

## 🏗️ Project Structure

```
pathfinding-visualizer/
├── src/
│   ├── algorithms/          # Algorithm implementations
│   │   ├── astar.py        # A* algorithm
│   │   └── dijkstra.py     # Dijkstra's algorithm
│   ├── core/               # Core data structures
│   │   ├── node.py         # Grid node representation
│   │   └── grid.py         # Grid management
│   ├── ui/                 # User interface components
│   │   ├── menu.py         # Main menu system
│   │   ├── visualizer.py   # Algorithm visualization
│   │   └── colors.py       # Color definitions
│   └── config/             # Configuration settings
│       └── settings.py     # Application settings
├── data/                   # Maze configuration files
├── assets/                 # Image assets
├── main.py                 # Application entry point
├── requirements.txt        # Python dependencies
└── README.md              # This file
```

## 🔧 Technical Details

- **Language**: Python 3.8+
- **Graphics**: Pygame 2.6.1
- **Architecture**: Modular design with separation of concerns
- **Algorithms**: Implemented with proper data structures (Priority Queue)
- **Visualization**: Real-time rendering with 60 FPS

## 📈 Performance Insights

The application measures and displays execution times, allowing you to observe:
- A* typically finds paths faster due to its heuristic guidance
- Dijkstra's explores more nodes but guarantees the shortest path
- Performance varies based on maze complexity and start/goal positions

## 🎓 Educational Value

This project demonstrates:
- **Search Algorithm Theory**: Practical implementation of graph search
- **Heuristic Functions**: Manhattan distance in pathfinding
- **Data Structures**: Priority queues, graphs, and 2D grids
- **Software Architecture**: Clean, maintainable code structure
- **Performance Analysis**: Algorithm comparison and optimization

## 🤝 Contributing

This project was developed as part of CS 530 (Artificial Intelligence) coursework. Feel free to fork and enhance!

## 📄 License

This project is open source and available under the [MIT License](LICENSE).

---

**Course**: CS 530 - Artificial Intelligence  
**Institution**: [Your University]  
**Academic Year**: [Year]