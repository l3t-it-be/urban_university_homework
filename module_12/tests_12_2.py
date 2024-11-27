import unittest

from module_12.runner_and_tournament import Runner, Tournament


class TournamentTest(unittest.TestCase):
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

    def test_race_usain_and_nick(self):
        tournament = Tournament(90, self.usain, self.nick)
        result = tournament.start()
        self.all_results['test_race_usain_and_nick'] = result
        self.assertTrue(result[max(result.keys())] == 'Ник')

    def test_race_andrey_and_nick(self):
        tournament = Tournament(90, self.andrey, self.nick)
        result = tournament.start()
        self.all_results['test_race_andrey_and_nick'] = result
        self.assertTrue(result[max(result.keys())] == 'Ник')

    def test_race_usain_andrey_and_nick(self):
        tournament = Tournament(90, self.usain, self.andrey, self.nick)
        result = tournament.start()
        self.all_results['test_race_usain_andrey_and_nick'] = result
        self.assertTrue(result[max(result.keys())] == 'Ник')


if __name__ == '__main__':
    unittest.main()
