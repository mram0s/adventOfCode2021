import unittest
from src.day1.sonarSweep import SonarSweep


class TestSonarSweep(unittest.TestCase):
    def test_should_return_the_increase_amount(self):
        report = [188, 192, 193, 194, 192, 213, 214]
        self.assertEqual(SonarSweep.get_increases_amount(report), 5)

    def test_should_return_the_sliding_window_increase_amount(self):
        report = [188, 192, 193, 194, 192, 213, 214]
        self.assertEqual(
            SonarSweep.get_sliding_window_increases_amount(report), 3)
