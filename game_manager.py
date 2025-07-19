import pygame
from objects.fighter import Fighter
from objects.alien import Alien
from constants import (
    ALIEN_ROWS, ALIEN_COLS, ALIEN_START_X, ALIEN_START_Y,
    ALIEN_SPACING_X, ALIEN_SPACING_Y, FIGHTER_SPEED, BLACK
)

class GameManager:
    def __init__(self):
        self.fighter = Fighter()
        self.aliens = []
        self.running = True
        self._create_alien_formation()
    
    def _create_alien_formation(self):
        """Create alien formation"""
        for y in range(ALIEN_ROWS):
            for x in range(ALIEN_COLS):
                alien = Alien()
                alien.set_position(
                    ALIEN_START_X + ALIEN_SPACING_X * x,
                    ALIEN_START_Y + ALIEN_SPACING_Y * y
                )
                self.aliens.append(alien)
    
    def handle_events(self):
        """Handle pygame events"""
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False
            elif event.type == pygame.KEYDOWN:
                self._handle_keydown(event.key)
    
    def _handle_keydown(self, key):
        """Handle key press events"""
        if key == pygame.K_LEFT:
            self.fighter.move(-FIGHTER_SPEED, 0)
        elif key == pygame.K_RIGHT:
            self.fighter.move(FIGHTER_SPEED, 0)
        elif key == pygame.K_UP:
            self.fighter.move(0, -FIGHTER_SPEED)
        elif key == pygame.K_DOWN:
            self.fighter.move(0, FIGHTER_SPEED)
    
    def update(self):
        """Update game state"""
        # TODO: 게임 로직 구현
        pass
    
    def render(self, surface):
        """Render all game objects"""
        surface.fill(BLACK)
        self.fighter.draw(surface)
        
        for alien in self.aliens:
            alien.draw(surface) 