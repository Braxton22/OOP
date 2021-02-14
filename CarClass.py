class Car:
    def __init__(self, year, make):
        self.__year_model = year
        self.__make = make
        self.__speed = 0

    def accelerate(self):
        self.__speed += 5
        return self.__speed

    def brake(self):
        if self.__speed < 5:
            self.__speed = "The car isn't moving"
        else:
            self.__speed -= 5
        return self.__speed

    def get_speed(self):
        return self.__speed
