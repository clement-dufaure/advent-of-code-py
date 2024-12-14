from unittest import TestCase

from main.advent_2024.day15 import part1, part2
from test.advent_2024 import get_input_test, get_input


class Day1Test(TestCase):
    def test_day15_part1_ex1(self):
        self.assertEqual(0, part1(get_input_test("day15")))

    def test_day15_part1(self):
        self.assertEqual(0, part1(get_input("day15")))

    def test_day15_part2_ex1(self):
        self.assertEqual(0, part2(get_input_test("day15")))

    def test_day15_part2(self):
        self.assertEqual(None, part2(get_input("day15")))
