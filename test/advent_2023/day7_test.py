from unittest import TestCase

from main.advent_2023.day7 import part1, part2
from test.advent_2023 import get_input_test, get_input


class Day1Test(TestCase):
    def test_day7_part1_ex1(self):
        self.assertEqual(6440, part1(get_input_test("day7")))

    def test_day7_part1(self):
        self.assertEqual(248396258, part1(get_input("day7")))

    def test_day7_part2_ex1(self):
        self.assertEqual(5905, part2(get_input_test("day7")))

    def test_day7_part2(self):
        self.assertEqual(246436046, part2(get_input("day7")))
