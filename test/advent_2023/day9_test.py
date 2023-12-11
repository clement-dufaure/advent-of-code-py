from unittest import TestCase

from main.advent_2023.day9 import part1, part2
from test.advent_2023 import get_input_test, get_input


class Day1Test(TestCase):
    def test_day8_part1_ex1(self):
        self.assertEqual(114, part1(get_input_test("day9")))

    def test_day8_part1(self):
        self.assertEqual(1842168671, part1(get_input("day9")))

    def test_day8_part2_ex1(self):
        self.assertEqual(2, part2(get_input_test("day9")))

    def test_day8_part2(self):
        self.assertEqual(903, part2(get_input("day9")))
