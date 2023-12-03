from unittest import TestCase

from main.advent_2023.day3 import part1, part2
from test.advent_2023 import get_input_test, get_input


class Day1Test(TestCase):
    def test_day2_part1_ex1(self):
        self.assertEqual(4361, part1(get_input_test("day3")))

    def test_day2_part1(self):
        self.assertEqual(557705, part1(get_input("day3")))

    def test_day2_part2_ex1(self):
        self.assertEqual(467835, part2(get_input_test("day3")))

    def test_day2_part2(self):
        self.assertEqual(84266818, part2(get_input("day3")))
