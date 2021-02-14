import CarClass as c

Ferarri = c.Car(2020, "California")

for n in range(1, 6):
    Ferarri.accelerate()
    print("The car is moving", Ferarri.get_speed(), "mph")

for k in range(1, 6):
    Ferarri.brake()
    print("The car is moving", Ferarri.get_speed(), "mph")
