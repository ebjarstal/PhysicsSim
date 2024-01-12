#  objects.py
import time
from typing import Type


class Point:

    position = None

    def __init__(self, start_position: tuple = (0, 0), start_speed: int = 0):
        self.creation_time = time.time()
        self.position = start_position
        self.speed = start_speed

    def is_colliding(self, other_point: Type["Point"]):
        return self.position == other_point.position

    def move(self, new_position: tuple):
        self.position = new_position

    def change_speed(self, new_speed: int):
        self.speed = new_speed


class Field(object):
    def __init__(self, dimensions: tuple = (100, 100)):
        self.dimensions: tuple = dimensions
        self.name: str = ""
