import unittest

from module_12.tests_12_1 import RunnerTest
from module_12.tests_12_2 import TournamentTest


def suite():
    test_suite = unittest.TestSuite()
    loader = unittest.TestLoader()

    test_suite.addTests(loader.loadTestsFromTestCase(RunnerTest))
    test_suite.addTests(loader.loadTestsFromTestCase(TournamentTest))

    return test_suite


if __name__ == '__main__':
    runner = unittest.TextTestRunner(verbosity=2)
    runner.run(suite())
