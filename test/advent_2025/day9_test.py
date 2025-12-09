from unittest import TestCase

from main.advent_2025.day9 import part1, part2
from test.advent_2025 import get_input_test, get_input


class Day1Test(TestCase):
    def test_day9_part1_ex1(self):
        self.assertEqual(50, part1(get_input_test("day9"),10))

    def test_day9_part1(self):
        self.assertEqual(4773451098, part1(get_input("day9"),1000))

    def test_day9_part2_ex1(self):
        self.assertEqual(24, part2(get_input_test("day9")))

    def test_day9_part2(self):
        self.assertEqual(1429075575, part2(get_input("day9")))
