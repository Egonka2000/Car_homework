import unittest
from car import Car

class TestCarIntegartion(unittest.TestCase):
    def setUp(self):
        self.car = Car("BMW", "Q7", 12000, 140, 70)
    
    def test_drive(self):
        self.car.fill_the_tank(70)
        self.car.change_the_speed(True, 60)
        consume = self.car.calculate_consume()

        self.car.drive(50, consume)
        self.assertEqual(self.car.fuel_level, 30)

        with self.assertRaises(ValueError):
            self.car.drive(100, consume)

if __name__ == "__main__":
    unittest.main()