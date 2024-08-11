import unittest
from Runner import Runner


class RunnerTest(unittest.TestCase):
    is_frozen = False

    @unittest.skipIf(is_frozen, "Тесты в этом кейсе заморожены")
    def test_walk(self):
        subject = Runner('example')
        for i in range(10):
            subject.walk()
        self.assertEqual(subject.distance, 50)

    @unittest.skipIf(is_frozen, "Тесты в этом кейсе заморожены")
    def test_run(self):
        subject = Runner('example')
        for i in range(10):
            subject.run()
        self.assertEqual(subject.distance, 100)

    @unittest.skipIf(is_frozen, "Тесты в этом кейсе заморожены")
    def test_challenge(self):
        subject_1 = Runner('challenger1')
        subject_2 = Runner('challenger2')
        for i in range(10):
            subject_1.walk()
            subject_2.run()
        self.assertNotEqual(subject_1.distance, subject_2.distance)