class Car():
    def __init__(self, brand, model, price, current_speed, fuel_capacity):
        self.brand = brand
        self.model = model
        self.price = price
        self.current_speed = current_speed
        self.fuel_capacity = fuel_capacity
        self.fuel_level = 0
    
    def fill_the_tank(self, fuel_liters):
        if fuel_liters < 0:
            raise ValueError("Can't append negative liters of fuel")
        elif self.fuel_level + fuel_liters > self.fuel_capacity:
            self.fuel_level = self.fuel_capacity
        else:
            self.fuel_level += fuel_liters

    def drive(self, distance, consume):
        fuel_needed = distance * consume
        if fuel_needed > self.fuel_level:
            raise ValueError("There is not enough fuel for this distance.")
        self.fuel_level -= fuel_needed
    
    def change_the_speed(self, late, speed):
        if late:
            self.current_speed += speed
        else:
            self.current_speed -= speed
    
    def calculate_consume(self):
        if self.current_speed < 100:
            consume = 0.3
        elif self.current_speed < 150:
            consume = 0.5
        else:
            consume = 0.8
        return consume