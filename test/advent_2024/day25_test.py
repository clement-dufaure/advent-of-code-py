from unittest import TestCase

from main.advent_2024.day25 import part1, part2
from test.advent_2024 import get_input_test, get_input


class Day1Test(TestCase):
    def test_day25_part1_ex1(self):
        self.assertEqual(3, part1(get_input_test("day25")))

    def test_day25_part1(self):
        self.assertEqual(3466, part1(get_input("day25")))
