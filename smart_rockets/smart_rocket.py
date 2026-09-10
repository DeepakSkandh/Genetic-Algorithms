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

    def update(self):
        force = self.dna.genes[self.time]

        self.acceleration += force
        self.velocity += self.acceleration
        self.position += self.velocity
        self.acceleration *= 0

        self.time += 1