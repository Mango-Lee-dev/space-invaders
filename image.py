import pygame
from game_objects.fighter import Fighter
from game_objects.alien import Alien

print("startup");

pygame.init()
pygame.key.set_repeat(500, 500)
surface = pygame.display.set_mode((640, 480))
clock = pygame.time.Clock()

fighter = Fighter()

aliens = []
for y in range(5):
  for x in range(12):
    alien = Alien()
    aliens.append(alien)
    alien.x = 70 + 50 * x
    alien.y = 100 + 70 * y

while True:
  print("Update") 
  for event in pygame.event.get():
    if event.type == pygame.QUIT:
      print("Shutdown")
      pygame.quit()
      exit()
      break

  print("Render")
  surface.fill((0, 0, 0))
  fighter.draw(surface)

  for alien in aliens:
    alien.draw(surface)
  pygame.display.update()
  clock.tick(30)