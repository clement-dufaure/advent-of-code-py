from unittest import TestCase

from main.advent_2024.day14 import part1, part2
from test.advent_2024 import get_input_test, get_input


class Day1Test(TestCase):
    def test_day14_part1_ex1(self):
        self.assertEqual(12, part1(get_input_test("day14"), 11, 7))

    def test_day14_part1(self):
        self.assertEqual(229421808, part1(get_input("day14"), 101, 103))

    #def test_day14_part2_ex1(self):
    #    self.assertEqual(0, part2(get_input_test("day14")))

    def test_day14_part2(self):
        self.assertEqual(None, part2(get_input("day14"), 101, 103))
