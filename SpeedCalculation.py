#Переписать код SpeedCalculation в соответствии с Open-Closed Principle

class SpeedCalculation:
    def calculate_allowed_speed(self, vehicle):
        return vehicle.calculate_allowed_speed()


class Vehicle:
    def __init__(self, max_speed, type):
        self.max_speed = max_speed
        self.type = type

    def get_max_speed(self):
        return self.max_speed

    def get_type(self):
        return self.type

    def calculate_allowed_speed(self):
        pass


class Car(Vehicle):
    def calculate_allowed_speed(self):
        return self.get_max_speed() * 0.8


class Bus(Vehicle):
    def calculate_allowed_speed(self):
        return self.get_max_speed() * 0.6