import math

class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def show(self):
        print(f"({self.x}, {self.y})")

    def move(self, x, y):
        self.x += x
        self.y += y

    def dist(self, x1 , y1 ):
        return ((self.x - self.x1)**2 + (self.y - self.y1)**2)**0.5