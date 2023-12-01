from unittest import TestCase

from main.advent_2023.day1 import part1, part2
from test.advent_2023 import get_input_test, get_input


class Day1Test(TestCase):
    def test_day1_part1_ex1(self):
        self.assertEqual(142, part1(get_input_test("day1")))

    def test_day1_part1(self):
        self.assertEqual(56049, part1(get_input("day1")))

    def test_day1_part2_ex1(self):
        self.assertEqual(281, part2(get_input_test("day1-1")))

    def test_day1_part2(self):
        self.assertEqual(54530, part2(get_input("day1")))
