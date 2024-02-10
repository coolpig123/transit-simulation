import pygame
import math


class Planet:
    G = 10

    def __init__(self, pos, rad, mass, color):
        self.pos = pos
        self.rad = rad
        self.mass = mass
        self.color = color

        self.vel = pygame.Vector2()

    def draw(self, screen):
        pygame.draw.circle(screen, self.color, self.pos, self.rad)

    def get_distance(self, other):
        distance_x = other.pos.x - self.pos.x
        distance_y = other.pos.y - self.pos.y
        distance = math.sqrt(distance_x ** 2 + distance_y ** 2)
        return distance

    def get_theta(self, other):
        distance_x = other.pos.x - self.pos.x
        distance_y = other.pos.y - self.pos.y
        theta = math.atan2(distance_y, distance_x)
        return theta

    def get_force(self, other):
        distance = self.get_distance(other)
        theta = self.get_theta(other)
        force_mag = self.G * self.mass * other.mass / distance ** 2
        force = pygame.Vector2(math.cos(theta) * force_mag, math.sin(theta) * force_mag)
        return force

    def update(self, other):
        force = self.get_force(other)

        self.vel.x += force.x / self.mass
        self.vel.y += force.y / self.mass

        self.pos.x += self.vel.x
        self.pos.y += self.vel.y
