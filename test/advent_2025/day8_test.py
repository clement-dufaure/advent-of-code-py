from unittest import TestCase

from main.advent_2025.day8 import part1, part2
from test.advent_2025 import get_input_test, get_input


class Day1Test(TestCase):
    def test_day8_part1_ex1(self):
        self.assertEqual(40, part1(get_input_test("day8"),10))

    def test_day8_part1(self):
        self.assertEqual(105952, part1(get_input("day8"),1000))

    def test_day8_part2_ex1(self):
        self.assertEqual(25272, part2(get_input_test("day8")))

    def test_day8_part2(self):
        self.assertEqual(975931446, part2(get_input("day8")))
