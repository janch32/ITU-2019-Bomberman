#!usr/bin/python3

# ITU projekt: hra Bomberman
#
# File: barell.py
# Author: Michal Krůl

from backend.modules.position import Position

class Barrel(Position):
    def __init__(self, x: int = 0, y: int = 0):
        self.position = Position.__init__(x, y)

    def getPosition(self):
        return self.position
