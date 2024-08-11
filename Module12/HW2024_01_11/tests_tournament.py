import unittest
from Tournament import Runner, Tournament


class TournamentTest(unittest.TestCase):

    is_frozen = True

    @classmethod
    def setUpClass(cls):
        cls.all_results = {}

    def setUp(self):
        self.runner1 = Runner('Усэйн', 10)
        self.runner2 = Runner('Андрей', 9)
        self.runner3 = Runner('Ник', 3)

    @classmethod
    def tearDownClass(cls):
        for result in cls.all_results.values():
            print(result)

    @unittest.skipIf(is_frozen, "Тесты в этом кейсе заморожены")
    def test_1(self):
        tour1 = Tournament(90, self.runner1, self.runner3)
        self.all_results[1] = tour1.start()
        self.assertTrue('Ник' in str(list(self.all_results[1].values())[-1]))

    @unittest.skipIf(is_frozen, "Тесты в этом кейсе заморожены")
    def test_2(self):
        tour2 = Tournament(90, self.runner2, self.runner3)
        self.all_results[2] = tour2.start()
        self.assertTrue('Ник' in str(list(self.all_results[2].values())[-1]))

    @unittest.skipIf(is_frozen, "Тесты в этом кейсе заморожены")
    def test_3(self):
        tour3 = Tournament(90, self.runner1, self.runner2, self.runner3)
        self.all_results[3] = tour3.start()
        self.assertTrue('Ник' in str(list(self.all_results[3].values())[-1]))


if __name__ == '__main__':
    unittest.main()
