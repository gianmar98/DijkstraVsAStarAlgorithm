# Development Guide

This document provides information for developers who want to understand, modify, or extend the Pathfinding Algorithm Visualizer.

## 🏗️ Architecture Overview

The project follows a modular architecture with clear separation of concerns:

### Core Components

- **`src/core/`**: Core data structures and game logic
  - `node.py`: Individual grid cell representation
  - `grid.py`: 2D grid management and file I/O

- **`src/algorithms/`**: Pathfinding algorithm implementations
  - `astar.py`: A* algorithm with Manhattan distance heuristic
  - `dijkstra.py`: Dijkstra's algorithm implementation

- **`src/ui/`**: User interface and visualization
  - `menu.py`: Main menu system for maze selection
  - `visualizer.py`: Real-time algorithm visualization
  - `colors.py`: Color constants and semantic mapping

- **`src/config/`**: Configuration and settings
  - `settings.py`: Application constants and maze configurations

## 🔧 Development Setup

### Prerequisites
- Python 3.8+
- Virtual environment (recommended)
- Git

### Setup Steps

1. **Clone and setup environment**
   ```bash
   git clone <repo-url>
   cd pathfinding-visualizer
   python3 -m venv venv
   source venv/bin/activate  # Windows: venv\Scripts\activate
   ```

2. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

3. **Verify installation**
   ```bash
   python test_installation.py
   ```

4. **Run the application**
   ```bash
   python main.py
   ```

## 📁 File Structure

```
pathfinding-visualizer/
├── src/                    # Source code
│   ├── algorithms/         # Algorithm implementations
│   ├── core/              # Core data structures
│   ├── ui/                # User interface
│   └── config/            # Configuration
├── data/                  # Maze data files
│   ├── A1.txt - A4.txt    # A* maze configurations
│   └── dijkstra1.txt - dijkstra4.txt  # Dijkstra maze configurations
├── assets/                # Image assets
│   ├── title.png          # Menu title image
│   └── firstLab.png - fourthLab.png   # Maze preview images
├── main.py               # Application entry point
├── test_installation.py  # Installation verification
├── requirements.txt      # Python dependencies
├── setup.py             # Package setup
└── README.md            # User documentation
```

## 🎨 Adding New Features

### Adding a New Algorithm

1. Create a new file in `src/algorithms/`
2. Implement the search function with signature:
   ```python
   def your_algorithm_search(draw_func, grid_nodes, start, goal) -> bool:
       # Your implementation
       pass
   ```
3. Update `src/ui/visualizer.py` to include your algorithm
4. Add configuration options in `src/config/settings.py`

### Adding New Maze Configurations

1. Create maze data files in `data/` directory
2. Add configuration to `LAB_CONFIGS` in `src/config/settings.py`
3. Add preview images to `assets/` directory
4. Update menu system in `src/ui/menu.py`

### Customizing Visualization

- Modify colors in `src/ui/colors.py`
- Adjust grid size and window dimensions in `src/config/settings.py`
- Customize drawing logic in `src/core/grid.py` and `src/core/node.py`

## 🧪 Testing

### Running Tests
```bash
python test_installation.py
```

### Manual Testing
1. Test all 4 maze configurations
2. Verify both algorithms work correctly
3. Check performance timing output
4. Test edge cases (no path scenarios)

### Adding Tests
- Add unit tests for new algorithms
- Test edge cases and error conditions
- Verify UI responsiveness

## 📊 Performance Considerations

### Algorithm Performance
- Both algorithms use Priority Queue for O(log n) insertions
- A* uses Manhattan distance heuristic for faster pathfinding
- Dijkstra's guarantees shortest path without heuristic

### Visualization Performance
- 60 FPS rendering with pygame
- Efficient grid drawing with minimal redraws
- Event handling prevents UI freezing during computation

## 🐛 Common Issues

### Import Errors
- Ensure virtual environment is activated
- Check that `src/` is in Python path
- Verify all `__init__.py` files exist

### File Not Found Errors
- Check that data files are in `data/` directory
- Verify image files are in `assets/` directory
- Ensure file paths in `settings.py` are correct

### Pygame Issues
- Install pygame: `pip install pygame`
- On some systems, may need additional dependencies
- Check pygame version compatibility

## 🚀 Deployment

### Creating Executable
```bash
pip install pyinstaller
pyinstaller --onefile --windowed main.py
```

### Package Distribution
```bash
python setup.py sdist bdist_wheel
```

## 📝 Code Style

- Follow PEP 8 Python style guidelines
- Use type hints where appropriate
- Document functions with docstrings
- Keep functions focused and modular
- Use meaningful variable names

## 🤝 Contributing

1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Add tests if applicable
5. Update documentation
6. Submit a pull request

## 📚 Learning Resources

- [A* Algorithm](https://en.wikipedia.org/wiki/A*_search_algorithm)
- [Dijkstra's Algorithm](https://en.wikipedia.org/wiki/Dijkstra%27s_algorithm)
- [Pygame Documentation](https://www.pygame.org/docs/)
- [Python Type Hints](https://docs.python.org/3/library/typing.html)