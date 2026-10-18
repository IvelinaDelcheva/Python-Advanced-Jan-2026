class Car:
    def __init__(self, make, model, fuel_consumption, fuel_capacity):
        self.make = make
        self.model = model
        self.fuel_consumption = fuel_consumption
        self.fuel_capacity = fuel_capacity
        self.fuel_amount = 0

    @property
    def make(self):
        return self.__make

    @make.setter
    def make(self, new_value):
        if not new_value:
            raise Exception("Make cannot be null or empty!")
        self.__make = new_value

    @property
    def model(self):
        return self.__model

    @model.setter
    def model(self, new_value):
        if not new_value:
            raise Exception("Model cannot be null or empty!")
        self.__model = new_value

    @property
    def fuel_consumption(self):
        return self.__fuel_consumption

    @fuel_consumption.setter
    def fuel_consumption(self, new_value):
        if new_value <= 0:
            raise Exception("Fuel consumption cannot be zero or negative!")
        self.__fuel_consumption = new_value

    @property
    def fuel_capacity(self):
        return self.__fuel_capacity

    @fuel_capacity.setter
    def fuel_capacity(self, new_value):
        if new_value <= 0:
            raise Exception("Fuel capacity cannot be zero or negative!")
        self.__fuel_capacity = new_value

    @property
    def fuel_amount(self):
        return self.__fuel_amount

    @fuel_amount.setter
    def fuel_amount(self, new_value):
        if new_value < 0:
            raise Exception("Fuel amount cannot be negative!")
        self.__fuel_amount = new_value

    def refuel(self, fuel):
        if fuel <= 0:
            raise Exception("Fuel amount cannot be zero or negative!")
        self.__fuel_amount += fuel
        if self.__fuel_amount > self.__fuel_capacity:
            self.__fuel_amount = self.__fuel_capacity

    def drive(self, distance):
        needed = (distance / 100) * self.__fuel_consumption

        if needed > self.__fuel_amount:
            raise Exception("You don't have enough fuel to drive!")

        self.__fuel_amount -= needed


# car = Car("a", "b", 1, 4)
# car.make = ""
# print(car)

from unittest import TestCase, main


class CarTests(TestCase):
    def setUp(self):
        self.car = Car("A", "B", 1, 10)

    def test_init(self):
        self.assertEqual("A", self.car.make)
        self.assertEqual("B", self.car.model)
        self.assertEqual(1, self.car.fuel_consumption)
        self.assertEqual(10, self.car.fuel_capacity)
        self.assertEqual(0, self.car.fuel_amount)

    def test_make_null_raises(self):
        with self.assertRaises(Exception) as ex:
            self.car = Car(None, "B", 1, 10)
        self.assertEqual("Make cannot be null or empty!", str(ex.exception))

    def test_make_empty_str_raises(self):
        with self.assertRaises(Exception) as ex:
            self.car = Car('', "B", 1, 10)
        self.assertEqual("Make cannot be null or empty!", str(ex.exception))

    def test_model_null_raises(self):
        with self.assertRaises(Exception) as ex:
            self.car = Car("A", None, 1, 10)
        self.assertEqual("Model cannot be null or empty!", str(ex.exception))

    def test_model_empty_str_raises(self):
        with self.assertRaises(Exception) as ex:
            self.car = Car("A", '', 1, 10)
        self.assertEqual("Model cannot be null or empty!", str(ex.exception))

    def test_fuel_consumption_0_raises(self):
        with self.assertRaises(Exception) as ex:
            self.car = Car("A", "B", 0, 10)
        self.assertEqual("Fuel consumption cannot be zero or negative!", str(ex.exception))

    def test_fuel_consumption_negative_raises(self):
        with self.assertRaises(Exception) as ex:
            self.car = Car("A", "B", -1, 10)
        self.assertEqual("Fuel consumption cannot be zero or negative!", str(ex.exception))

    def test_fuel_capacity_0_raises(self):
        with self.assertRaises(Exception) as ex:
            self.car = Car("A", "B", 1, 0)
        self.assertEqual("Fuel capacity cannot be zero or negative!", str(ex.exception))

    def test_fuel_capacity_negative_raises(self):
        with self.assertRaises(Exception) as ex:
            self.car = Car("A", "B", 1, -1)
        self.assertEqual("Fuel capacity cannot be zero or negative!", str(ex.exception))

    def test_fuel_amount_negative_raises(self):
        with self.assertRaises(Exception) as ex:
            self.car.fuel_amount = -10
        self.assertEqual("Fuel amount cannot be negative!", str(ex.exception))

    def test_fuel_amount(self):
        self.car.fuel_amount = 10
        self.assertEqual(10, self.car.fuel_amount)

    def test_refuel_with_fuel_0_and_negative(self):
        with self.assertRaises(Exception) as e:
            self.car.refuel(0)
        self.assertEqual("Fuel amount cannot be zero or negative!", str(e.exception))

        with self.assertRaises(Exception) as e:
            self.car.refuel(-1)
        self.assertEqual("Fuel amount cannot be zero or negative!", str(e.exception))




if __name__ == '__main__':
    main()
