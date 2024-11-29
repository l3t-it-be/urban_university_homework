import unittest


def skip_if_frozen(cls_name):
    def decorator(func):
        def wrapper(*args, **kwargs):
            cls = globals()[cls_name]
            if cls.is_frozen:
                raise unittest.SkipTest('Тесты в этом кейсе заморожены')
            return func(*args, **kwargs)

        return wrapper

    return decorator


class Runner:
    def __init__(self, name):
        self.name = name
        self.distance = 0

    def run(self):
        self.distance += 10

    def walk(self):
        self.distance += 5

    def __str__(self):
        return self.name


class RunnerTest(unittest.TestCase):
    is_frozen = False

    @skip_if_frozen('RunnerTest')
    def test_walk(self):
        runner = Runner('TestWalkRunner')
        for _ in range(10):
            runner.walk()
        self.assertEqual(runner.distance, 50)

    @skip_if_frozen('RunnerTest')
    def test_run(self):
        runner = Runner('TestRunRunner')
        for _ in range(10):
            runner.run()
        self.assertEqual(runner.distance, 100)

    @skip_if_frozen('RunnerTest')
    def test_challenge(self):
        runner1 = Runner('TestChallengeRunner1')
        runner2 = Runner('TestChallengeRunner2')
        for _ in range(10):
            runner1.run()
            runner2.walk()
        self.assertNotEqual(runner1.distance, runner2.distance)


if __name__ == '__main__':
    unittest.main()
