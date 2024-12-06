from unittest import TestCase

from main.advent_2024.day6 import part1, part2
from test.advent_2024 import get_input_test, get_input


class Day1Test(TestCase):
    def test_day6_part1_ex1(self):
        self.assertEqual(41, part1(get_input_test("day6")))

    def test_day6_part1(self):
        self.assertEqual(5086, part1(get_input("day6")))

    def test_day6_part2_ex1(self):
        self.assertEqual(6, part2(get_input_test("day6")))

    # 19 s
    def test_day6_part2(self):
        self.assertEqual(1770, part2(get_input("day6")))
