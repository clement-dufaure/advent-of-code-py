from unittest import TestCase

from main.advent_2022.day1 import part1, part2
from test.advent_2022 import get_input


class Day1Test(TestCase):
    def test_day1_part1(self):
        self.assertEqual(68923, part1(get_input("day1")))

    def test_day1_part2(self):
        self.assertEqual(200044, part2(get_input("day1")))
