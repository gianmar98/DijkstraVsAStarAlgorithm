"""
Menu system for selecting maze configurations.
"""

import pygame
import sys
from src.config.settings import (
    MENU_WIDTH, MENU_HEIGHT, DEFAULT_IMAGE_SIZE, IMAGES
)


class Menu:
    """
    Main menu for selecting maze configurations.
    """
    
    def __init__(self):
        """Initialize the menu system."""
        pygame.init()
        self.screen = pygame.display.set_mode((MENU_WIDTH, MENU_HEIGHT))
        pygame.display.set_caption("MENU -> CHOOSE A LABYRINTH")
        self.clock = pygame.time.Clock()
        self.running = True
        self.selected_lab = None
        
        # Load and scale images
        self.images = self._load_images()
    
    def _load_images(self) -> dict:
        """Load and scale all menu images."""
        images = {}
        try:
            # Load title image
            images['title'] = pygame.image.load(IMAGES['title'])
            images['title'] = pygame.transform.scale(images['title'], (MENU_WIDTH, 150))
            
            # Load lab images
            for i in range(1, 5):
                key = f'lab{i}'
                images[key] = pygame.image.load(IMAGES[key])
                images[key] = pygame.transform.scale(images[key], DEFAULT_IMAGE_SIZE)
                
        except pygame.error as e:
            print(f"Warning: Could not load image: {e}")
            # Create placeholder surfaces if images fail to load
            for key in ['title', 'lab1', 'lab2', 'lab3', 'lab4']:
                if key not in images:
                    size = (MENU_WIDTH, 150) if key == 'title' else DEFAULT_IMAGE_SIZE
                    images[key] = pygame.Surface(size)
                    images[key].fill((100, 100, 100))  # Gray placeholder
        
        return images
    
    def _get_image_positions(self) -> dict:
        """Calculate positions for all images."""
        return {
            'title': (0, 0),
            'lab1': (0, 150),
            'lab2': (MENU_WIDTH // 2, 150),
            'lab3': (0, (MENU_WIDTH // 2) + 150),
            'lab4': (MENU_WIDTH // 2, (MENU_WIDTH // 2) + 150)
        }
    
    def handle_events(self) -> None:
        """Handle pygame events."""
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False
                pygame.quit()
                sys.exit()
            
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_1:
                    self.selected_lab = 1
                    self.running = False
                elif event.key == pygame.K_2:
                    self.selected_lab = 2
                    self.running = False
                elif event.key == pygame.K_3:
                    self.selected_lab = 3
                    self.running = False
                elif event.key == pygame.K_4:
                    self.selected_lab = 4
                    self.running = False
    
    def draw(self) -> None:
        """Draw the menu screen."""
        # Clear screen
        self.screen.fill((0, 0, 0))
        
        # Draw all images
        positions = self._get_image_positions()
        for key, image in self.images.items():
            self.screen.blit(image, positions[key])
        
        # Update display
        pygame.display.flip()
    
    def run(self) -> int:
        """
        Run the menu and return selected lab number.
        
        Returns:
            Selected lab number (1-4) or None if quit
        """
        while self.running:
            self.handle_events()
            self.draw()
            self.clock.tick(60)  # 60 FPS
        
        return self.selected_lab