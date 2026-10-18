from unittest import TestCase, main

from project.cat import Cat


class CatTests(TestCase):
    def setUp(self):
        self.cat = Cat('Cat Name')

    def test_init(self):
        self.assertEqual('Cat Name', self.cat.name)
        self.assertFalse(self.cat.fed)
        self.assertFalse(self.cat.sleepy)
        self.assertEqual(0, self.cat.size)

        self.cat.fed = True
        self.cat.sleepy = True
        self.cat.size = 1

        self.assertTrue(self.cat.fed)
        self.assertTrue(self.cat.sleepy)
        self.assertEqual(1, self.cat.size)

    def test_eat_cat_size_increase(self):
        self.assertEqual(0, self.cat.size)
        self.cat.eat()
        self.assertEqual(1, self.cat.size)

    def test_cat_eat_fed_true(self):
        self.assertFalse(self.cat.fed)
        self.cat.eat()
        self.assertTrue(self.cat.fed)

    def test_cat_eat_fed_true_raises(self):
        self.assertFalse(self.cat.fed)
        self.cat.fed = True
        self.assertTrue(self.cat.fed)
        with self.assertRaises(Exception) as ex:
            self.cat.eat()
        self.assertEqual('Already fed.', str(ex.exception))
        self.assertTrue(self.cat.fed)
        self.cat.fed = False
        self.assertFalse(self.cat.fed)
        self.cat.eat()
        self.assertTrue(self.cat.sleepy)

    def test_cat_sleep_not_fed_raises(self):
        self.assertFalse(self.cat.fed)
        with self.assertRaises(Exception) as ex:
            self.cat.sleep()
        self.assertEqual('Cannot sleep while hungry', str(ex.exception))

    def test_cat_sleep_not_sleepy(self):
        self.cat.fed = True
        self.assertTrue(self.cat.fed)
        self.cat.sleepy = True
        self.assertTrue(self.cat.sleepy)
        self.cat.sleep()
        self.assertFalse(self.cat.sleepy)

if __name__ == '__main__':
    main()
