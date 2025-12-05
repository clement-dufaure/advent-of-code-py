from unittest import TestCase

from main.advent_2025.day3 import part1, part2
from test.advent_2025 import get_input_test, get_input


class Day1Test(TestCase):
    def test_day3_part1_ex1(self):
        self.assertEqual(357, part1(get_input_test("day3")))

    def test_day3_part1(self):
        self.assertEqual(17403, part1(get_input("day3")))

    def test_day3_part2_ex1(self):
        self.assertEqual(3121910778619, part2(get_input_test("day3")))

    def test_day3_part2(self):
        self.assertEqual(173416889848394, part2(get_input("day3")))
