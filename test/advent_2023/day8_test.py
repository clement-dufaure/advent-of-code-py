from unittest import TestCase

from main.advent_2023.day8 import part1, part2
from test.advent_2023 import get_input_test, get_input


class Day1Test(TestCase):
    def test_day8_part1_ex1(self):
        self.assertEqual(2, part1(get_input_test("day8-1")))

    def test_day8_part1_ex2(self):
        self.assertEqual(6, part1(get_input_test("day8-2")))

    def test_day8_part1(self):
        self.assertEqual(13207, part1(get_input("day8")))

    def test_day8_part2_ex1(self):
        self.assertEqual(6, part2(get_input_test("day8-3")))

    def test_day8_part2(self):
        self.assertEqual(12324145107121, part2(get_input("day8")))
