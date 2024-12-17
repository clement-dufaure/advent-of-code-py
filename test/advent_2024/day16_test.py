from unittest import TestCase

from main.advent_2024.day16 import part1, part2
from test.advent_2024 import get_input_test, get_input


class Day1Test(TestCase):
    def test_day16_part1_ex1(self):
        self.assertEqual(7036, part1(get_input_test("day16")))

    def test_day16_part1_ex2(self):
        self.assertEqual(11048, part1(get_input_test("day16-1")))

    def test_day16_part1(self):
        self.assertEqual(104516, part1(get_input("day16")))

    def test_day16_part2_ex1(self):
        self.assertEqual(45, part2(get_input_test("day16")))

    def test_day16_part2_ex2(self):
        self.assertEqual(64, part2(get_input_test("day16-1")))

    def test_day16_part2(self):
        self.assertEqual(545, part2(get_input("day16")))
