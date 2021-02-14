import random


class Insect:
    def __init__(self, w, l, f):
        self.__wings = w
        self.__legs = l
        self.__flight = f

    def flight_length(self):
        self.__flight = random.randint(1, 10)
        return self.__flight

    def __str__(self):
        return (
            "wings: "
            + str(self.__wings)
            + "\n"
            + "legs: "
            + str(self.__legs)
            + "\n"
            + "flight: "
            + str(self.__flight)
        )
