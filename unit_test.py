import unittest
from car import Car

class TestCar(unittest.TestCase):
    def setUp(self):
        self.car = Car("Toyota", "Corolla", 3000, 70, 50)

    def test_fill_the_tank(self):
        self.car.fill_the_tank(20)
        self.assertEqual(self.car.fuel_level, 20)

        self.car.fill_the_tank(40)
        self.assertEqual(self.car.fuel_level, self.car.fuel_capacity)

        with self.assertRaises(ValueError):
            self.car.fill_the_tank(-5)

    def test_change_the_speed(self):
        self.car.change_the_speed(True, 50)
        self.assertEqual(self.car.current_speed, 120)
        
        self.car.change_the_speed(False, 30)
        self.assertEqual(self.car.current_speed, 90)

if __name__ == "__main__":
    unittest.main()