from unittest import TestCase

from main.advent_2024.day3 import part1, part2
from test.advent_2024 import get_input_test, get_input


class Day1Test(TestCase):
    def test_day3_part1_ex1(self):
        self.assertEqual(161, part1(get_input_test("day3")))

    def test_day3_part1(self):
        self.assertEqual(175700056, part1(get_input("day3")))

    def test_day3_part2_ex1(self):
        self.assertEqual(48, part2(get_input_test("day3-1")))

    def test_day3_part2(self):
        self.assertEqual(71668682, part2(get_input("day3")))
