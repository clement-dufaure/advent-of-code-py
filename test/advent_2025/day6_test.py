from unittest import TestCase

from main.advent_2025.day6 import part1, part2
from test.advent_2025 import get_input_test, get_input


class Day1Test(TestCase):
    def test_day6_part1_ex1(self):
        self.assertEqual(4277556, part1(get_input_test("day6")))

    def test_day6_part1(self):
        self.assertEqual(3261038365331, part1(get_input("day6")))

    def test_day6_part2_ex1(self):
        self.assertEqual(3263827, part2(get_input_test("day6")))

    def test_day6_part2(self):
        self.assertEqual(8342588849093, part2(get_input("day6")))
