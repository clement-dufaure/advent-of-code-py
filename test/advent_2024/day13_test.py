from unittest import TestCase

from main.advent_2024.day13 import part1, part2
from test.advent_2024 import get_input_test, get_input


class Day1Test(TestCase):
    def test_day13_part1_ex1(self):
        self.assertEqual(480, part1(get_input_test("day13")))

    def test_day13_part1(self):
        self.assertEqual(35082, part1(get_input("day13")))

    def test_day13_part2_ex1(self):
        self.assertEqual(875318608908, part2(get_input_test("day13")))

    def test_day13_part2(self):
        self.assertEqual(82570698600470, part2(get_input("day13")))
