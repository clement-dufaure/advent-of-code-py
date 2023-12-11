from unittest import TestCase

from main.advent_2023.day11 import part1, part2
from test.advent_2023 import get_input_test, get_input


class Day1Test(TestCase):
    def test_day11_part1_ex1(self):
        self.assertEqual(374, part1(get_input_test("day11")))

    def test_day11_part1(self):
        self.assertEqual(9233514, part1(get_input("day11")))

    def test_day11_part2_ex2(self):
        self.assertEqual(1030, part2(get_input_test("day11"), coeff=10))

    def test_day11_part2_ex3(self):
        self.assertEqual(8410, part2(get_input_test("day11"), coeff=100))

    def test_day11_part2(self):
        self.assertEqual(363293506944, part2(get_input("day11")))
