from unittest import TestCase

from main.advent_2024.day7 import part1, part2
from test.advent_2024 import get_input_test, get_input


class Day1Test(TestCase):
    def test_day7_part1_ex1(self):
        self.assertEqual(3749, part1(get_input_test("day7")))

    def test_day7_part1(self):
        self.assertEqual(267566105056, part1(get_input("day7")))

    def test_day7_part2_ex1(self):
        self.assertEqual(11387, part2(get_input_test("day7")))

    # 20s
    def test_day7_part2(self):
        self.assertEqual(116094961956019, part2(get_input("day7")))
