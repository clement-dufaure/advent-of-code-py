from unittest import TestCase

from main.advent_2023.day2 import part1, part2
from test.advent_2023 import get_input_test, get_input


class Day1Test(TestCase):
    def test_day2_part1_ex1(self):
        self.assertEqual(8, part1(get_input_test("day2")))

    def test_day1_part1(self):
        self.assertEqual(2679, part1(get_input("day2")))

    def test_day1_part2_ex1(self):
        self.assertEqual(2286, part2(get_input_test("day2")))

    def test_day1_part2(self):
        self.assertEqual(77607, part2(get_input("day2")))
