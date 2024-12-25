from unittest import TestCase

from main.advent_2024.day21 import part1
from test.advent_2024 import get_input_test, get_input


class Day1Test(TestCase):
    def test_day21_part1_ex1(self):
        self.assertEqual(126384, part1(get_input_test("day21")))

    def test_day21_part1(self):
        self.assertEqual(188384, part1(get_input("day21")))

    def test_alt_day21_part2(self):
        self.assertEqual(232389969568832, part1(get_input("day21"), nb_pads=25))
