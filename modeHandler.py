from planet import Planet
import pygame
import math


def handle_orbit_1():
    sun = Planet(pygame.Vector2(400, 400), 50, 500, (255, 0, 0))
    planets = [Planet(pygame.Vector2(300, 400), 10, 5, (127, 127, 255))]

    for p in planets:
        p.vel.y = math.sqrt(p.G * sun.mass / p.get_distance(sun))

    return sun, planets


def handle_kepler_1():
    sun = Planet(pygame.Vector2(600, 400), 50, 500, (255, 0, 0))
    planets = [Planet(pygame.Vector2(300, 400), 10, 5, (127, 127, 255))]

    for p in planets:
        r = p.get_distance(sun)
        a = 300
        p.vel.y = math.sqrt(p.G * (p.mass * sun.mass) * (2 / r - 1 / a))

    return sun, planets


def handle_orbit_2_close():
    sun = Planet(pygame.Vector2(400, 400), 50, 500, (255, 0, 0))
    planets = [Planet(pygame.Vector2(400, 400), 10, 5, (172, 172, 255)),
               Planet(pygame.Vector2(380, 400), 10, 5, (222, 184, 135))]

    for p in planets:
        p.vel.y = math.sqrt(p.G * sun.mass / p.get_distance(sun))

    return sun, planets


def handle_orbit_2_far():
    sun = Planet(pygame.Vector2(400, 400), 50, 500, (255, 0, 0))
    planets = [Planet(pygame.Vector2(540, 400), 10, 5, (172, 172, 255)),
               Planet(pygame.Vector2(380, 400), 10, 5, (222, 184, 135))]

    for p in planets:
        p.vel.y = math.sqrt(p.G * sun.mass / p.get_distance(sun))

    return sun, planets


def handle_orbit_3_close():
    sun = Planet(pygame.Vector2(400, 400), 50, 500, (255, 0, 0))
    planets = [Planet(pygame.Vector2(400, 400), 10, 5, (0, 0, 255)),
               Planet(pygame.Vector2(100, 400), 50, 5, (255, 192, 203)),
               Planet(pygame.Vector2(380, 400), 10, 5, (222, 184, 135))]

    for p in planets:
        p.vel.y = math.sqrt(p.G * sun.mass / p.get_distance(sun))

    return sun, planets


def handle_orbit_3_far():
    sun = Planet(pygame.Vector2(400, 400), 50, 500, (255, 0, 0))
    planets = [Planet(pygame.Vector2(600, 400), 20, 5, (0, 0, 255)),
               Planet(pygame.Vector2(50, 400), 10, 5, (255, 192, 203)),
               Planet(pygame.Vector2(500, 400), 10, 5, (222, 184, 135))]

    for p in planets:
        p.vel.y = math.sqrt(p.G * sun.mass / p.get_distance(sun))

    return sun, planets


def set_mode():

    modes = {"orbit-1": handle_orbit_1,
             "kepler-1": handle_kepler_1,
             "orbit-2-close": handle_orbit_2_close,
             "orbit-2-far": handle_orbit_2_far,
             "orbit-3-close": handle_orbit_3_close,
             "orbit-3-far": handle_orbit_3_far}

    mode = input("Enter desired mode:")

    while mode not in modes.keys():
        mode = input("Enter desired mode:")

    return modes[mode]()
