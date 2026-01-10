#!/usr/bin/env python3
"""
Test script to verify the pathfinding visualizer installation.
"""

import sys
import os

def test_imports():
    """Test that all modules can be imported."""
    print("Testing imports...")
    
    try:
        import pygame
        print("✓ Pygame imported successfully")
    except ImportError as e:
        print(f"✗ Failed to import pygame: {e}")
        return False
    
    # Add src to path
    sys.path.insert(0, os.path.join(os.path.dirname(__file__), 'src'))
    
    try:
        from src.core.node import Node
        from src.core.grid import Grid
        from src.algorithms.astar import astar_search
        from src.algorithms.dijkstra import dijkstra_search
        from src.ui.menu import Menu
        from src.ui.visualizer import PathfindingVisualizer
        from src.config.settings import LAB_CONFIGS
        print("✓ All custom modules imported successfully")
    except ImportError as e:
        print(f"✗ Failed to import custom modules: {e}")
        return False
    
    return True

def test_files():
    """Test that required files exist."""
    print("\\nTesting file structure...")
    
    required_files = [
        'data/A1.txt', 'data/A2.txt', 'data/A3.txt', 'data/A4.txt',
        'data/dijkstra1.txt', 'data/dijkstra2.txt', 'data/dijkstra3.txt', 'data/dijkstra4.txt',
        'assets/title.png', 'assets/firstLab.png', 'assets/secondLab.png', 
        'assets/thirdLab.png', 'assets/fourthLab.png'
    ]
    
    missing_files = []
    for file_path in required_files:
        if os.path.exists(file_path):
            print(f"✓ {file_path}")
        else:
            print(f"✗ {file_path} (missing)")
            missing_files.append(file_path)
    
    return len(missing_files) == 0

def test_basic_functionality():
    """Test basic functionality without GUI."""
    print("\\nTesting basic functionality...")
    
    try:
        sys.path.insert(0, os.path.join(os.path.dirname(__file__), 'src'))
        from src.core.node import Node
        from src.core.grid import Grid
        
        # Test Node creation
        node = Node(0, 0, 10, 50)
        print("✓ Node creation works")
        
        # Test Grid creation
        grid = Grid(10, 100)
        print("✓ Grid creation works")
        
        # Test node positioning
        pos = node.get_position()
        assert pos == (0, 0), f"Expected (0, 0), got {pos}"
        print("✓ Node positioning works")
        
        return True
    except Exception as e:
        print(f"✗ Basic functionality test failed: {e}")
        return False

def main():
    """Run all tests."""
    print("=" * 50)
    print("PATHFINDING VISUALIZER - INSTALLATION TEST")
    print("=" * 50)
    
    all_passed = True
    
    # Run tests
    all_passed &= test_imports()
    all_passed &= test_files()
    all_passed &= test_basic_functionality()
    
    print("\\n" + "=" * 50)
    if all_passed:
        print("🎉 ALL TESTS PASSED! The installation is working correctly.")
        print("\\nYou can now run the application with: python main.py")
    else:
        print("❌ SOME TESTS FAILED. Please check the errors above.")
        print("\\nMake sure you have:")
        print("1. Activated the virtual environment: source venv/bin/activate")
        print("2. Installed dependencies: pip install -r requirements.txt")
        print("3. All data and asset files are in the correct directories")
    print("=" * 50)

if __name__ == "__main__":
    main()