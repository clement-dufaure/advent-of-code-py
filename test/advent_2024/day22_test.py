from unittest import TestCase

from main.advent_2024.day22 import part1, part2
from test.advent_2024 import get_input_test, get_input


class Day1Test(TestCase):
    def test_day22_part1_ex1(self):
        self.assertEqual(37327623, part1(get_input_test("day22")))

    def test_day22_part1(self):
        self.assertEqual(20215960478, part1(get_input("day22")))

    def test_day22_part2_ex1(self):
        self.assertEqual(23, part2(get_input_test("day22-1")))

    # 1min
    def test_day22_part2(self):
        self.assertEqual(0, part2(get_input("day22")))
