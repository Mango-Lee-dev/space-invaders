import pygame
from objects.fighter import Fighter
from objects.alien import Alien
from constants import (
    ALIEN_ROWS, ALIEN_COLS, ALIEN_START_X, ALIEN_START_Y,
    ALIEN_SPACING_X, ALIEN_SPACING_Y, FIGHTER_SPEED, BLACK, FPS
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
    
    def handle_events(self, clock):
        """Handle pygame events"""
        delta_seconds = clock.tick(FPS) / 1000
        
        keys = pygame.key.get_pressed()
        dx, dy = 0, 0
        
        if keys[pygame.K_LEFT]:
            dx = -1
        elif keys[pygame.K_RIGHT]:
            dx = 1
        if keys[pygame.K_UP]:
            dy = -1
        elif keys[pygame.K_DOWN]:
            dy = 1
        
        # delta_seconds를 활용한 자연스러운 움직임
        distance_x = FIGHTER_SPEED * dx * delta_seconds
        distance_y = FIGHTER_SPEED * dy * delta_seconds
        
        if dx != 0 or dy != 0:
            self.fighter.move(distance_x, distance_y)
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False
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