from unittest import TestCase

from main.advent_2024.day4 import part1, part2
from test.advent_2024 import get_input_test, get_input


class Day1Test(TestCase):
    def test_day4_part1_ex1(self):
        self.assertEqual(18, part1(get_input_test("day4")))

    def test_day4_part1(self):
        self.assertEqual(2517, part1(get_input("day4")))

    def test_day4_part2_ex1(self):
        self.assertEqual(9, part2(get_input_test("day4")))

    def test_day4_part2(self):
        self.assertEqual(1960, part2(get_input("day4")))
