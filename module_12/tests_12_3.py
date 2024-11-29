import unittest

from module_12.runner_and_tournament import Tournament, Runner


def skip_if_frozen(cls_name):
    def decorator(func):
        def wrapper(*args, **kwargs):
            cls = globals()[cls_name]
            if cls.is_frozen:
                raise unittest.SkipTest('Тесты в этом кейсе заморожены')
            return func(*args, **kwargs)

        return wrapper

    return decorator


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


class TournamentTest(unittest.TestCase):
    is_frozen = True

    all_results = {}

    @classmethod
    def setUpClass(cls):
        cls.all_results = {}

    def setUp(self):
        self.usain = Runner('Усэйн', 10)
        self.andrey = Runner('Андрей', 9)
        self.nick = Runner('Ник', 3)

    @classmethod
    def tearDownClass(cls):
        for result in cls.all_results.values():
            formatted_result = {
                place: str(runner) for place, runner in result.items()
            }
            print(formatted_result)

    @skip_if_frozen('TournamentTest')
    def test_race_usain_and_nick(self):
        tournament = Tournament(90, self.usain, self.nick)
        result = tournament.start()
        self.all_results['test_race_usain_and_nick'] = result
        self.assertTrue(result[max(result.keys())] == 'Ник')

    @skip_if_frozen('TournamentTest')
    def test_race_andrey_and_nick(self):
        tournament = Tournament(90, self.andrey, self.nick)
        result = tournament.start()
        self.all_results['test_race_andrey_and_nick'] = result
        self.assertTrue(result[max(result.keys())] == 'Ник')

    @skip_if_frozen('TournamentTest')
    def test_race_usain_andrey_and_nick(self):
        tournament = Tournament(90, self.usain, self.andrey, self.nick)
        result = tournament.start()
        self.all_results['test_race_usain_andrey_and_nick'] = result
        self.assertTrue(result[max(result.keys())] == 'Ник')


if __name__ == '__main__':
    unittest.main()
