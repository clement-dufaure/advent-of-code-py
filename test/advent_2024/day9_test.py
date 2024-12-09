from unittest import TestCase

from main.advent_2024.day9 import part1, part2
from test.advent_2024 import get_input_test, get_input


class Day1Test(TestCase):
    def test_day9_part1_ex1(self):
        self.assertEqual(1928, part1(get_input_test("day9")))

    def test_day9_part1(self):
        self.assertEqual(6382875730645, part1(get_input("day9")))

    def test_day9_part2_ex1(self):
        self.assertEqual(2858, part2(get_input_test("day9")))

    # 4s
    def test_day9_part2(self):
        self.assertEqual(6420913943576, part2(get_input("day9")))
