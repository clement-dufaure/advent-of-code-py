from unittest import TestCase

from main.advent_2023.day6 import part1, part2
from test.advent_2023 import get_input_test, get_input


class Day1Test(TestCase):
    def test_day6_part1_ex1(self):
        self.assertEqual(288, part1(get_input_test("day6")))

    def test_day6_part1(self):
        self.assertEqual(138915, part1(get_input("day6")))

    def test_day6_part2_ex1(self):
        self.assertEqual(71503, part2(get_input_test("day6")))

    def test_day6_part2(self):
        self.assertEqual(27340847, part2(get_input("day6")))
