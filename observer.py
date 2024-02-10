from shapely.geometry import Point
from shapely.geometry.polygon import Polygon
from os import environ
environ['PYGAME_HIDE_SUPPORT_PROMPT'] = '1'
import pygame
import math


class Observer:
    def __init__(self, pos):
        self.pos = pos

    def get_tangent_points(self, planet):
        (Px, Py) = (self.pos.x, self.pos.y)
        (Cx, Cy) = (planet.pos.x, planet.pos.y)
        a = planet.rad

        b = math.sqrt((Px - Cx) ** 2 + (Py - Cy) ** 2)
        th = math.acos(a / b)  # angle theta
        d = math.atan2(Py - Cy, Px - Cx)
        d1 = d + th
        d2 = d - th

        pt1 = pygame.Vector2(Cx + a * math.cos(d1), Cy + a * math.sin(d1))
        pt2 = pygame.Vector2(Cx + a * math.cos(d2), Cy + a * math.sin(d2))

        return pt1, pt2

    def draw_tangents(self, screen, sun):
        pt1, pt2 = self.get_tangent_points(sun)

        pygame.draw.line(screen, (255, 255, 255), self.pos, pt1, width=1)
        pygame.draw.line(screen, (255, 255, 255), self.pos, pt2, width=1)

    @staticmethod
    def calc_distance(pt1, pt2):
        return math.sqrt((pt2.x - pt1.x) ** 2 + (pt2.y - pt1.y) ** 2)

    @staticmethod
    def pts_to_line(pt1, pt2):
        a = pt1.y - pt2.y
        b = pt2.x - pt1.x
        c = (pt1.x * pt2.y - pt2.x * pt1.y)
        return a, b, c

    @staticmethod
    def check_collision(a, b, c, x, y, radius):
        dist = ((abs(a * x + b * y + c)) / math.sqrt(a * a + b * b))
        if radius == dist or radius > dist:
            return True
        else:
            return False

    def get_light_percentage(self, sun, planet):
        pt1, pt2 = self.get_tangent_points(sun)

        point = Point(planet.pos.x, planet.pos.y)
        polygon = Polygon([(pt1.x, pt1.y), (pt2.x, pt2.y), (self.pos.x, self.pos.y)])

        if polygon.contains(point):
            return (planet.rad / sun.rad) ** 2
        else:
            return 0
