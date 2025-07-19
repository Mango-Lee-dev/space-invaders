import pygame
from constants import SCREEN_WIDTH, SCREEN_HEIGHT, FIGHTER_START_X, FIGHTER_START_Y

class Fighter:
  def __init__(self):
    image = pygame.image.load("assets/images/fighter.png")
    self.scale_up_image = pygame.transform.scale(image, (image.get_width() * 2, image.get_height() * 2))
    self.x = FIGHTER_START_X - self.scale_up_image.get_width() // 2
    self.y = FIGHTER_START_Y

  def move(self, dx, dy):
    """Move fighter by given delta values"""
    self.x += dx
    self.y += dy
    
    # Keep fighter within screen bounds
    self.x = max(0, min(self.x, SCREEN_WIDTH - self.scale_up_image.get_width()))
    self.y = max(0, min(self.y, SCREEN_HEIGHT - self.scale_up_image.get_height()))

  def draw(self, surface):
    surface.blit(self.scale_up_image, (self.x, self.y))