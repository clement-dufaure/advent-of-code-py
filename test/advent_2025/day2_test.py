from unittest import TestCase

from main.advent_2025.day2 import part1, part2
from test.advent_2025 import get_input_test, get_input


class Day1Test(TestCase):
    def test_day2_part1_ex1(self):
        self.assertEqual(1227775554, part1(get_input_test("day2")))

    def test_day2_part1(self):
        self.assertEqual(1102, part1(get_input("day2")))

    def test_day2_part2_ex1(self):
        self.assertEqual(4174379265, part2(get_input_test("day2")))

    def test_day2_part2(self):
        self.assertEqual(41823587546, part2(get_input("day2")))
