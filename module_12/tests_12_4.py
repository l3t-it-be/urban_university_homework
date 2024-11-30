import unittest
import logging

from module_12.HumanMoveTest import Runner

# Настройка логирования
logging.basicConfig(
    level=logging.INFO,
    filename='runner_tests.log',
    filemode='w',
    encoding='UTF-8',
    format='%(levelname)s: %(asctime)s - %(filename)s - %(message)s',
)


class RunnerTest(unittest.TestCase):

    def test_walk(self):
        runner = Runner('TestWalkRunner')
        for _ in range(10):
            runner.walk()
        self.assertEqual(runner.distance, 50)
        logging.info('"test_walk" выполнен успешно')

    def test_run(self):
        runner = Runner('TestRunRunner')
        for _ in range(10):
            runner.run()
        self.assertEqual(runner.distance, 100)
        logging.info('"test_run" выполнен успешно')

    def test_challenge(self):
        runner1 = Runner('TestChallengeRunner1')
        runner2 = Runner('TestChallengeRunner2')
        for _ in range(10):
            runner1.run()
            runner2.walk()
        self.assertNotEqual(runner1.distance, runner2.distance)

    @staticmethod
    def test_invalid_speed():
        try:
            Runner(
                'TestInvalidSpeedRunner', speed=-5
            )  # Передаем отрицательное значение в speed
        except ValueError as e:
            logging.warning(
                f'Неверная скорость для Runner: {e}', exc_info=True
            )
            raise  # Выбрасываем исключение, чтобы тест завершился с ошибкой

    @staticmethod
    def test_invalid_name():
        try:
            Runner(2)  # Передаем int вместо str
        except TypeError as e:
            logging.warning(
                f'Неверный тип данных для объекта Runner: {e}', exc_info=True
            )
            raise  # Выбрасываем исключение, чтобы тест завершился с ошибкой


if __name__ == '__main__':
    unittest.main()
