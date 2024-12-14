from unittest import TestCase

from main.advent_2024.day11 import part1, part2
from test.advent_2024 import get_input_test, get_input


class Day1Test(TestCase):
    def test_day11_part1_ex1(self):
        self.assertEqual(55312, part1(get_input_test("day11")))

    def test_day11_part1(self):
        self.assertEqual(203953, part1(get_input("day11")))

    # def test_day11_part2_ex1(self):
    #    self.assertEqual(55312, part2(get_input_test("day11")))

    def test_day11_part2(self):
        self.assertEqual(242090118578155, part2(get_input("day11")))
