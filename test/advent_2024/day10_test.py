from unittest import TestCase

from main.advent_2024.day10 import part1, part2
from test.advent_2024 import get_input_test, get_input


class Day1Test(TestCase):
    def test_day10_part1_ex1(self):
        self.assertEqual(36, part1(get_input_test("day10")))

    def test_day10_part1(self):
        self.assertEqual(694, part1(get_input("day10")))

    def test_day10_part2_ex1(self):
        self.assertEqual(81, part2(get_input_test("day10")))

    def test_day10_part2(self):
        self.assertEqual(1497, part2(get_input("day10")))
