#!usr/bin/python3

# ITU projekt: hra Bomberman
#
# File: obstacle.py
# Author: Michal Krůl

from modules.position import Position

class Obstacle(Position):
    def __init__(self, x: int = 0, y: int = 0):
        Position.__init__(self, x, y)
