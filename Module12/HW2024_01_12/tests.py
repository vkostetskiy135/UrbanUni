
import unittest
import logging
import logger
import Students

class TestStudents(unittest.TestCase):

    def test_walk(self):
        """
        Тест для метода walk() в main.Student
        :return:
        """
        example = Students.Student('example')
        for i in range(10):
            example.walk()
        try:
            self.assertEqual(example.distance, 50, 'Дистанции не равны!')
            logging.info(f'Метод walk() корректно!')
        except AssertionError:
            logging.error(f'Получил неожиданный результат в методе walk()!: {example.distance}\n', exc_info=True)
            raise

    def test_run(self):
        """
        Тест для метода run() в main.Student
        :return:
        """
        example = Students.Student('example')
        for i in range(10):
            example.run()
        try:
            self.assertEqual(example.distance, 100, 'Дистанции не равны!')
            logging.info(f'Метод run() работает корректно!')
        except AssertionError:
            logging.error(f'Получил неожиданный результат в методе run()!: {example.distance}\n', exc_info=True)
            raise

    def test_walk_run_comparison(self):
        '''
        Тест на реалистичность
        :return:
        '''
        student1 = Students.Student('student1')
        student2 = Students.Student('student2')
        for i in range(10):
            student1.walk()
            student2.run()
        try:
            self.assertLess(student1.distance, student2.distance,
                            msg=f'Бегущий человек {student2.name} : {student2.distance} должен преодолеть дистанцию'
                                f'больше, чем идущий человек {student1.name} : {student1.distance}')
            logging.info(f'Сравнение результатов соответствует ожиданиям!')
        except AssertionError:
            logging.error(f'Ожидалось что бегущий человек преодолеет большую дистанцию, чем идущий!', exc_info=True)
            raise




