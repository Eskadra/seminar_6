#Переписать код в соответствии с Dependency Inversion Principle
from abc import ABC, abstractmethod

class Engine(ABC):
    @abstractmethod
    def start(self):
        pass

class PetrolEngine(Engine):
    def start(self):
        print("Пуск бензинового двигателя")

class DieselEngine(Engine):
    def start(self):
        print("Пуск дизельного двигателя")

class Car:
    def __init__(self, engine):
        self.engine = engine

    def start(self):
        self.engine.start()