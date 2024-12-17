from unittest import TestCase

from main.advent_2024.day18 import part1, part2
from test.advent_2024 import get_input_test, get_input


class Day1Test(TestCase):
    def test_day18_part1_ex1(self):
        self.assertEqual(0, part1(get_input_test("day18")))

    def test_day18_part1(self):
        self.assertEqual(0, part1(get_input("day18")))

    def test_day18_part2_ex1(self):
        self.assertEqual(0, part2(get_input_test("day18")))

    def test_day18_part2(self):
        self.assertEqual(0, part2(get_input("day18")))
