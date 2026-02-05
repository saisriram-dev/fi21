# Perfect example of encapsulation + polymorphism + inheritance
class FareStrategy:
    def calculate(self, km):
        pass

class NormalFare(FareStrategy):
    def calculate(self, km):
        return km * 10

class SurgeFare(FareStrategy):
    def calculate(self, km):
        return km * 18

class Ride:
    def __init__(self, strategy):
        self.strategy = strategy

    def price(self, km):
        return self.strategy.calculate(km)
