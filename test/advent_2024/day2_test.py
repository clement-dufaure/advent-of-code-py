from unittest import TestCase

from main.advent_2024.day2 import part1, part2
from test.advent_2024 import get_input_test, get_input


class Day1Test(TestCase):
    def test_day2_part1_ex1(self):
        self.assertEqual(2, part1(get_input_test("day2")))

    def test_day2_part1(self):
        self.assertEqual(257, part1(get_input("day2")))

    def test_day2_part2_ex1(self):
        self.assertEqual(4, part2(get_input_test("day2")))

    def test_day2_part2(self):
        self.assertEqual(328, part2(get_input("day2")))
