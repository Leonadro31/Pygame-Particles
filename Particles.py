import pygame, random

SCREEN_HEIGHT = 1000
SCREEN_WIDTH = 700

clock = pygame.time.Clock()
win = pygame.display.set_mode((SCREEN_HEIGHT, SCREEN_WIDTH))

particles = []

class Particle(object):
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.speed_x = random.randint(-5, 5)
        self.speed_y = -random.randint(5, 15)
        self.size = random.randint(5, 10)
        self.gravity = random.randint(1, 8)
        self.color = (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))


    def draw(self, surface):
        self.move()
        pygame.draw.circle(surface, self.color, (self.x, self.y), self.size)

    def move(self):
        self.x += self.speed_x
        self.y += self.speed_y
        self.y += self.gravity
        self.size -= 0.3

        if self.size <= 0:
            del self




running = True
while running:
    clock.tick(60)

    win.fill((0, 0, 0))


    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    mouse_pos = pygame.mouse.get_pos()
    
    for i in range(5):
        particles.append(Particle(mouse_pos[0], mouse_pos[1]))

    for particle in particles[:]:
        if particle.size <= 0:
            particles.remove(particle)
            del particle
        else:
            particle.draw(win)


    pygame.display.update()

pygame.quit()

    
   
  
