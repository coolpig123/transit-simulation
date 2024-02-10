from planet import Planet
import pygame
import math


def handle_orbit_1():
    sun = Planet(pygame.Vector2(400, 400), 50, 500, (255, 0, 0))
    planets = [Planet(pygame.Vector2(300, 400), 10, 5, (127, 127, 255))]

    for p in planets:
        p.vel.y = math.sqrt(p.G * sun.mass / p.get_distance(sun))
        print(f'Initial velocity of planet is {p.vel.y}')

    return sun, planets


def handle_orbit_2():
    sun = Planet(pygame.Vector2(400, 400), 50, 500, (255, 0, 0))
    planets = [Planet(pygame.Vector2(100, 400), 10, 5, (172, 172, 255)),
               Planet(pygame.Vector2(150, 400), 10, 5, (222, 184, 135))]

    i = 0
    for p in planets:
        p.vel.y = math.sqrt(p.G * sun.mass / p.get_distance(sun))
        print(f'Initial velocity of planet {i} is {p.vel.y}')
        i += 1

    return sun, planets


def handle_orbit_3():
    sun = Planet(pygame.Vector2(400, 400), 50, 500, (255, 0, 0))
    planets = [Planet(pygame.Vector2(200, 400), 10, 5, (0, 0, 255)),
               Planet(pygame.Vector2(100, 400), 25, 5, (255, 192, 203)),
               Planet(pygame.Vector2(300, 400), 5, 5, (222, 184, 135))]

    i = 0
    for p in planets:
        p.vel.y = math.sqrt(p.G * sun.mass / p.get_distance(sun))
        print(f'Initial velocity of planet {i} is {p.vel.y}')
        i += 1

    return sun, planets


def handle_kepler_1():
    # initial_velocity = 1.6431676725154982

    sun = Planet(pygame.Vector2(600, 400), 50, 400, (255, 0, 0))
    planets = [Planet(pygame.Vector2(100, 400), 10, 5, (127, 127, 255))]

    for p in planets:
        r = p.get_distance(sun)
        a = 300
        p.vel.y = math.sqrt(p.G * (p.mass + sun.mass) * (2 / r - 1 / a))
        print(f'Initial velocity of planet is {p.vel.y}')

    return sun, planets


def set_mode():
    modes = {"orbit-1": handle_orbit_1,
             "orbit-2": handle_orbit_2,
             "orbit-3": handle_orbit_3,
             "kepler-1": handle_kepler_1}

    mode = input("Enter desired mode:")

    while mode not in modes.keys():
        mode = input("Enter desired mode:")

    return modes[mode](), mode
