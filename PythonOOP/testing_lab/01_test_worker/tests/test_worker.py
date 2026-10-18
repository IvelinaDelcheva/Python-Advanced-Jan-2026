from project.worker import Worker
from unittest import TestCase, main

class WorkerTests(TestCase):
    def setUp(self):
        self.worker = Worker('Test Name', 1000, 50)

    def test_init(self):
        self.assertEqual('Test Name', self.worker.name)
        self.assertEqual(1000, self.worker.salary)
        self.assertEqual(50, self.worker.energy)
        self.assertEqual(0, self.worker.money)

        self.worker.money = 500
        self.assertEqual(500, self.worker.money)

    def test_rest(self):
        self.assertEqual(50, self.worker.energy)
        self.worker.rest()
        self.assertEqual(51, self.worker.energy)

    def test_worker_works_no_energy_raises(self):
        self.worker.energy = 0
        self.assertEqual(0, self.worker.energy)
        with self.assertRaises(Exception) as ex:
            self.worker.work()
        self.assertEqual('Not enough energy.', str(ex.exception))

        self.worker.energy = -1
        self.assertEqual(-1, self.worker.energy)
        with self.assertRaises(Exception) as ex:
            self.worker.work()
        self.assertEqual('Not enough energy.', str(ex.exception))

    def test_worker_works_salary_increase(self):
        self.assertEqual(0, self.worker.money)
        self.worker.work()
        self.assertEqual(1000, self.worker.money)

    def test_worker_works_energy_decrease(self):
        self.assertEqual(50, self.worker.energy)
        self.worker.work()
        self.assertEqual(49, self.worker.energy)

    def test_worker_get_info(self):
        self.assertEqual('Test Name', self.worker.name)
        self.assertEqual(0, self.worker.money)
        self.worker.get_info()
        self.assertEqual('Test Name has saved 0 money.', self.worker.get_info())



if __name__ == '__main__':
    main()
