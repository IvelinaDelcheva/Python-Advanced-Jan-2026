from unittest import TestCase, main

from project.vehicle import Vehicle


class VehicleTest(TestCase):
    DEFAULT_FUEL_CONSUMPTION = 1.25
    fuel = 10.0
    horse_power = 100.0

    def setUp(self):
        self.vehicle = Vehicle(self.fuel, self.horse_power)

    def test_init(self):
        self.assertEqual(self.fuel, self.vehicle.fuel)
        self.assertEqual(self.fuel, self.vehicle.capacity)
        self.assertEqual(self.horse_power, self.vehicle.horse_power)
        self.assertEqual(self.DEFAULT_FUEL_CONSUMPTION, self.vehicle.fuel_consumption)

    def test_drive_success(self):
        self.vehicle.drive(2)
        self.assertEqual(7.5, self.vehicle.fuel)

    def test_drive_not_enough_fuel(self):
        with self.assertRaises(Exception) as e:
            self.vehicle.drive(10)
        self.assertEqual("Not enough fuel", str(e.exception))

    def test_refuel_success(self):
        self.vehicle.fuel = 5
        self.vehicle.refuel(5)
        self.assertEqual(self.fuel, self.vehicle.fuel)

    def test_refuel_too_much_fuel(self):
        self.vehicle.fuel = 5
        with self.assertRaises(Exception) as e:
            self.vehicle.refuel(8)
        self.assertEqual("Too much fuel", str(e.exception))

    def test_str(self):
        expected = f"The vehicle has {self.horse_power} " \
                   f"horse power with {self.fuel} fuel left and {self.DEFAULT_FUEL_CONSUMPTION} fuel consumption"
        self.assertEqual(expected, str(self.vehicle))


if __name__ == '__main__':
    main()
