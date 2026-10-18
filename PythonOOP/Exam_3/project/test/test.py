from unittest import TestCase, main
from project.star_system import StarSystem


class StarSystemTest(TestCase):
    def setUp(self):
        self.ss1 = StarSystem('s1', 'Red giant', 'Single', 9)
        self.ss2 = StarSystem('s2', 'Blue giant', 'Binary', 9, (2, 3))

    def test_init(self):
        self.assertEqual('s1', self.ss1.name)
        self.assertEqual('Red giant', self.ss1.star_type)
        self.assertEqual('Single', self.ss1.system_type)
        self.assertEqual(9, self.ss1.num_planets)
        self.assertEqual(None, self.ss1.habitable_zone_range)

    def test_is_habitable(self):
        self.assertFalse(self.ss1.is_habitable)

    def test_is_habitable_true(self):
        self.ss1.habitable_zone_range = (1, 5)
        self.assertTrue(self.ss1.is_habitable)

    def test_name_empty_str(self):
        with self.assertRaises(ValueError) as e:
            self.ss1.name = '   '
        self.assertEqual("Name must be a non-empty string.", str(e.exception))

    def test_start_type_not_in(self):
        with self.assertRaises(ValueError) as e:
            self.ss1.star_type = 'Unknown'
        self.assertEqual(
            f"Star type must be one of ['Blue giant', 'Brown dwarf', 'Red dwarf', 'Red giant', 'Yellow dwarf'].",
            str(e.exception))

    def test_system_type_not_in(self):
        with self.assertRaises(ValueError) as e1:
            self.ss1.system_type = 'Unknown'
        self.assertEqual(f"System type must be one of ['Binary', 'Multiple', 'Single', 'Triple'].", str(e1.exception))

    def test_num_of_planets_lt_0(self):
        with self.assertRaises(ValueError) as e:
            self.ss1.num_planets = -1
        self.assertEqual("Number of planets must be a non-negative integer.", str(e.exception))

    def test_habitable_zone_range_property(self):
        self.assertEqual(None, self.ss1.habitable_zone_range)

    def test_habitable_zone_range(self):
        with self.assertRaises(ValueError) as e:
            self.ss1.habitable_zone_range = (1, 2, 3)
        self.assertEqual("Habitable zone range must be a tuple of two numbers (start, end) where start < end.",
                         str(e.exception))

        with self.assertRaises(ValueError) as e:
            self.ss1.habitable_zone_range = (3, 3)
        self.assertEqual("Habitable zone range must be a tuple of two numbers (start, end) where start < end.",
                         str(e.exception))

        with self.assertRaises(ValueError) as e:
            self.ss1.habitable_zone_range = (3, 2)
        self.assertEqual("Habitable zone range must be a tuple of two numbers (start, end) where start < end.",
                         str(e.exception))

    def test_gt(self):
        with self.assertRaises(ValueError) as e:
            print(self.ss1 > self.ss2)
        self.assertEqual('Comparison not possible: One or both systems lack a defined habitable zone or planets.', str(e.exception))

    def test_gt_success(self):
        self.ss1.habitable_zone_range = (2, 8)
        self.ss2.habitable_zone_range = (3, 6)
        self.assertTrue(self.ss1 > self.ss2)

    def test_gt_false(self):
        self.ss1.habitable_zone_range = (2, 6)
        self.ss2.habitable_zone_range = (3, 8)
        self.assertFalse(self.ss1 > self.ss2)

    def test_compare_star_systems(self):
        self.ss1.habitable_zone_range = (2, 10)
        self.ss2.habitable_zone_range = (3, 6)
        expected = StarSystem.compare_star_systems(self.ss1, self.ss2)
        self.assertEqual("s1 has a wider habitable zone than s2.", expected)

        self.ss1.habitable_zone_range = (3, 4)
        self.ss2.habitable_zone_range = (2, 10)
        expected = StarSystem.compare_star_systems(self.ss1, self.ss2)
        self.assertEqual("s2 has a wider or equal habitable zone compared to s1.", expected)

        self.ss1.habitable_zone_range = None
        self.ss2.habitable_zone_range = None
        with self.assertRaises(ValueError) as e:
            StarSystem.compare_star_systems(self.ss1, self.ss2)
        self.assertEqual(ValueError, e)




if __name__ == '__main__':
    main()
