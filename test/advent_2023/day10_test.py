from unittest import TestCase

from main.advent_2023.day10 import part1, part2
from test.advent_2023 import get_input_test, get_input


class Day1Test(TestCase):
    def test_day10_part1_ex1(self):
        self.assertEqual(4, part1(get_input_test("day10-1")))

    def test_day10_part1_ex2(self):
        self.assertEqual(8, part1(get_input_test("day10-2")))

    def test_day10_part1(self):
        self.assertEqual(6882, part1(get_input("day10")))

    def test_day10_part2_ex1(self):
        self.assertEqual(4, part2(get_input_test("day10-3")))

    def test_day10_part2_ex2(self):
        self.assertEqual(4, part2(get_input_test("day10-4")))

    def test_day10_part2_ex3(self):
        self.assertEqual(8, part2(get_input_test("day10-5")))

    def test_day10_part2_ex4(self):
        self.assertEqual(10, part2(get_input_test("day10-6")))

    def test_day10_part2(self):
        self.assertEqual(491, part2(get_input("day10")))
