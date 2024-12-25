from unittest import TestCase

from main.advent_2024.day19 import part1, part2
from test.advent_2024 import get_input_test, get_input


class Day1Test(TestCase):
    def test_day19_part1_ex1(self):
        self.assertEqual(6, part1(get_input_test("day19")))

    def test_day19_part1(self):
        self.assertEqual(220, part1(get_input("day19")))

    def test_day19_part2_ex1(self):
        self.assertEqual(16, part2(get_input_test("day19")))

    # 11s
    def test_day19_part2(self):
        self.assertEqual(565600047715343, part2(get_input("day19")))
