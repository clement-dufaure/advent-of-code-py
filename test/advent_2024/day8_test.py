from unittest import TestCase

from main.advent_2024.day8 import part1, part2
from test.advent_2024 import get_input_test, get_input


class Day1Test(TestCase):
    def test_day8_part1_ex1(self):
        self.assertEqual(14, part1(get_input_test("day8")))

    def test_day8_part1(self):
        self.assertEqual(357, part1(get_input("day8")))

    def test_day8_part2_ex1(self):
        self.assertEqual(34, part2(get_input_test("day8")))

    def test_day8_part2(self):
        self.assertEqual(1266, part2(get_input("day8")))
