class IntegerList:
    def __init__(self, *args):
        self.__data = []
        for x in args:
            if type(x) == int:
                self.__data.append(x)

    def get_data(self):
        return self.__data

    def add(self, element):
        if not type(element) == int:
            raise ValueError("Element is not Integer")
        self.get_data().append(element)
        return self.get_data()

    def remove_index(self, index):
        if index >= len(self.get_data()):
            raise IndexError("Index is out of range")
        a = self.get_data()[index]
        del self.get_data()[index]
        return a

    def get(self, index):
        if index >= len(self.get_data()):
            raise IndexError("Index is out of range")
        return self.get_data()[index]

    def insert(self, index, el):
        if index >= len(self.get_data()):
            raise IndexError("Index is out of range")
        elif not type(el) == int:
            raise ValueError("Element is not Integer")

        self.get_data().insert(index, el)

    def get_biggest(self):
        a = sorted(self.get_data(), reverse=True)
        return a[0]

    def get_index(self, el):
        return self.get_data().index(el)

from unittest import TestCase, main

class IntegerListTests(TestCase):
    def setUp(self):
        self.ls = IntegerList()

    def test_init(self):
        self.assertEqual([], self.ls.get_data())
        self.ls = IntegerList(1, 2 , 3)
        self.assertEqual([1, 2 , 3], self.ls.get_data())
        self.ls = IntegerList(1, 2, '3')
        self.assertEqual([1, 2], self.ls.get_data())

    def test_add_not_int_raises(self):
        self.assertEqual([], self.ls.get_data())
        with self.assertRaises(Exception) as ex:
            self.ls.add('1')
            self.assertEqual("Element is not Integer", str(ex.exception))
        self.assertEqual([], self.ls.get_data())

    def test_add_return_list(self):
        self.assertEqual([], self.ls.get_data())
        self.ls.add(1)
        self.assertEqual([1], self.ls.get_data())

    def test_remove_index_out_of_range_raises(self):
        self.ls.get_data().extend([1, 2, 3])
        self.assertEqual([1, 2, 3], self.ls.get_data())
        with self.assertRaises(Exception) as ex:
            self.ls.remove_index(3)
        self.assertEqual("Index is out of range", str(ex.exception))


    def test_get_index_out_of_range_raises(self):
        self.ls.get_data().extend([1, 2, 3])
        self.assertEqual([1, 2, 3], self.ls.get_data())
        with self.assertRaises(Exception) as ex:
            self.ls.get(3)
        self.assertEqual("Index is out of range", str(ex.exception))

    def test_integer_list_remove_index(self):
        self.ls.get_data().extend([1, 2, 3])
        self.assertEqual([1, 2, 3], self.ls.get_data())
        self.assertEqual(1, self.ls.remove_index(0))
        self.assertEqual([2, 3], self.ls.get_data())

    def test_integer_list_get(self):
        self.ls.get_data().extend([1, 2, 3])
        self.assertEqual([1, 2, 3], self.ls.get_data())
        self.ls.get(2)
        self.assertEqual(3, self.ls.get_data()[2])

    def test_insert_index_out_of_range_raises(self):
        self.ls.get_data().extend([1, 2, 3])
        self.assertEqual([1, 2, 3], self.ls.get_data())
        with self.assertRaises(Exception) as ex:
            self.ls.insert(3, 4)
        self.assertEqual("Index is out of range", str(ex.exception))
        self.assertEqual([1, 2, 3], self.ls.get_data())


    def test_insert_not_int_raises(self):
        self.ls.get_data().extend([1, 2, 3])
        self.assertEqual([1, 2, 3], self.ls.get_data())
        with self.assertRaises(Exception) as ex:
            self.ls.insert(2, '4')
        self.assertEqual("Element is not Integer", str(ex.exception))
        self.assertEqual([1, 2, 3], self.ls.get_data())

    def test_integer_list_insert(self):
        self.ls.get_data().extend([1, 2, 3])
        self.assertEqual([1, 2, 3], self.ls.get_data())
        self.ls.insert(2, 4)
        self.assertEqual([1, 2, 4, 3], self.ls.get_data())

    def test_integer_list_get_biggest(self):
        self.ls.get_data().extend([1, 2, 4, 3])
        self.assertEqual([1, 2, 4, 3], self.ls.get_data())
        self.assertEqual(4, self.ls.get_biggest())

    def test_integer_list_get_index(self):
        self.ls.get_data().extend([1, 2, 4, 3])
        self.assertEqual([1, 2, 4, 3], self.ls.get_data())
        self.assertEqual(1, self.ls.get_index(2))


if __name__ == '__main__':
    main()