from unittest import TestCase

from main.advent_2025.day4 import part1, part2
from test.advent_2025 import get_input_test, get_input


class Day1Test(TestCase):
    def test_day4_part1_ex1(self):
        self.assertEqual(13, part1(get_input_test("day4")))

    def test_day4_part1(self):
        self.assertEqual(1533, part1(get_input("day4")))

    def test_day4_part2_ex1(self):
        self.assertEqual(43, part2(get_input_test("day4")))

    def test_day4_part2(self):
        self.assertEqual(9206, part2(get_input("day4")))
