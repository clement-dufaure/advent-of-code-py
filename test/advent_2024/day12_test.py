from unittest import TestCase

from main.advent_2024.day12 import part1, part2
from test.advent_2024 import get_input_test, get_input


class Day1Test(TestCase):
    def test_day12_part1_ex1(self):
        self.assertEqual(140, part1(get_input_test("day12")))

    def test_day12_part1_ex2(self):
        self.assertEqual(772, part1(get_input_test("day12-1")))

    def test_day12_part1_ex3(self):
        self.assertEqual(1930, part1(get_input_test("day12-2")))

    def test_day12_part1(self):
        self.assertEqual(1518548, part1(get_input("day12")))

    def test_day12_part2_ex1(self):
        self.assertEqual(80, part2(get_input_test("day12")))

    def test_day12_part2_ex2(self):
        self.assertEqual(436, part2(get_input_test("day12-1")))

    def test_day12_part2_ex3(self):
        self.assertEqual(236, part2(get_input_test("day12-3")))

    def test_day12_part2_ex4(self):
        self.assertEqual(368, part2(get_input_test("day12-4")))

    def test_day12_part2_ex5(self):
        self.assertEqual(1206, part2(get_input_test("day12-2")))

    def test_day12_part2(self):
        self.assertEqual(909564, part2(get_input("day12")))
