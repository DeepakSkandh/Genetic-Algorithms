import pygame 
import random

class DNA:
    def __init__(self, length):
        self.genes = []

        for _ in range(length):
            force = pygame.Vector2(
                random.uniform(-1, 1),
                random.uniform(-1, 1)
            )

            self.genes.append(force)

class Rocket:
    def __init__(self, x, y, dna):
        self.position = pygame.Vector2(x, y)
        self.velocity = pygame.Vector2(0, 0)
        self.acceleration = pygame.Vector2(0, 0)

        self.dna = dna
        self.time = 0

        self.image = pygame.image.load("assets/rocket.png").convert_alpha()
        self.image = pygame.transform.scale(self.image, (30, 50))

    def draw(self, screen):
        screen.blit(self.image, self.position)

    def update(self):
        if self.time < len(self.dna.genes):
            force = self.dna.genes[self.time]
            self.acceleration += force
            self.time += 1
        self.velocity += self.acceleration
        self.position += self.velocity
        self.acceleration *= 0

        

class Population:
    def __init__(self,size,dna_length,x,y):
        self.rockets = []
        for _ in range(size):
            dna = DNA(dna_length)
            rocket = Rocket(x,y,dna)
            self.rockets.append(rocket)
    def draw(self, screen):
        for rocket in self.rockets:
            rocket.draw(screen)
    def update(self):
        for rocket in self.rockets:
            rocket.update()


def main():
    pygame.init()

    screen = pygame.display.set_mode((1400,900))
    pygame.display.set_caption("Smart Rockets")

    clock = pygame.time.Clock()
    running = True

    population = Population(size=20,dna_length=200,x=400,y=550)

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        population.update()
        screen.fill((0, 0, 0))
        population.draw(screen)

        pygame.display.flip()
        clock.tick(60)

    pygame.quit()


if __name__ == "__main__":
    main()
