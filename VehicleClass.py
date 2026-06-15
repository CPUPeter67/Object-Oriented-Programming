class Vehicle:
    def __init__ (self, max_speed, mileage):
        self.max_speed = max_speed
        self.mileage = mileage

modelx = Vehicle(250, 14)

print("The max speed of this car model is:", modelx.max_speed, "mph.")
print("The mileage of this car model is:", modelx.mileage, "mpg.")
