#Переписать код в соответствии с Interface Segregation Principle

from abc import ABC, abstractmethod
import math

class AreaCalculable(ABC):
    @abstractmethod
    def calculate_area(self):
        pass

class VolumeCalculable(ABC):
    @abstractmethod
    def calculate_volume(self):
        pass

class Circle(AreaCalculable):
    def __init__(self, radius):
        self.radius = radius

    def calculate_area(self):
        return 2 * math.pi * self.radius

class Cube(AreaCalculable, VolumeCalculable):
    def __init__(self, edge):
        self.edge = edge

    def calculate_area(self):
        return 6 * self.edge * self.edge

    def calculate_volume(self):
        return self.edge * self.edge * self.edge