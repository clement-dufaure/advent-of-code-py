from unittest import TestCase

from main.advent_2023.day5 import part1, part2
from test.advent_2023 import get_input_test, get_input


class Day1Test(TestCase):
    def test_day5_part1_ex1(self):
        self.assertEqual(35, part1(get_input_test("day5")))

    def test_day5_part1(self):
        self.assertEqual(35, part1(get_input("day5")))

    def test_day5_part2_ex1(self):
        self.assertEqual(46, part2(get_input_test("day5")))

    def test_day5_part2(self):
        self.assertEqual(26714516, part2(get_input("day5")))
