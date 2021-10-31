from project.vehicle import Vehicle
from unittest import TestCase, main


class TestVehicle(TestCase):
    def setUp(self):
        self.v = Vehicle(100, 100)


    def test_valid_inputs(self):
        obj = Vehicle(1.5, 1.5)
        a = obj.fuel
        b = obj.horse_power
        self.assertTrue(isinstance(a, float))
        self.assertTrue(isinstance(b, float))

    def test_creating_instance(self):
        obj = Vehicle(100, 100)
        self.assertEqual(100, obj.fuel)
        self.assertEqual(100, obj.horse_power)
        self.assertEqual(100, obj.capacity)
        self.assertEqual(1.25, obj.fuel_consumption)
        self.assertEqual(1.25, obj.DEFAULT_FUEL_CONSUMPTION)

    def test_drive_correct_distance(self):
        obj = Vehicle(100, 100)
        obj.drive(10)
        self.assertEqual(87.5, obj.fuel)

    def test_drive_with_incorrect_distance(self):
        obj = Vehicle(100, 100)
        with self.assertRaises(Exception) as ex:
            obj.drive(100)
        self.assertEqual("Not enough fuel", str(ex.exception))

    def test_refuel_with_correct_value(self):
        obj = Vehicle(100, 100)
        obj.drive(10)
        obj.refuel(10)
        self.assertEqual(97.5, obj.fuel)

    def test_refuel_with_incorrect_value(self):
        obj = Vehicle(100, 100)
        with self.assertRaises(Exception) as ex:
            obj.refuel(3000)
        self.assertEqual("Too much fuel", str(ex.exception))

    def test_str_representation(self):
        obj = Vehicle(100, 100)
        self.assertEqual(f"The vehicle has 100 "
                         f"horse power with 100 fuel left and 1.25 fuel consumption", str(obj))


if __name__ == "__main__":
    main()