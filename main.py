import pygame
from game_manager import GameManager
from constants import SCREEN_WIDTH, SCREEN_HEIGHT, FPS

def main():
	"""Main game function"""
	pygame.init()
	pygame.key.set_repeat(500, 500)
	
	surface = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
	clock = pygame.time.Clock()
	
	game = GameManager()
	
	while game.running:
		game.handle_events()
		game.update()
		game.render(surface)
		
		pygame.display.update()
		clock.tick(FPS)
	
	pygame.quit()

if __name__ == "__main__":
  main()