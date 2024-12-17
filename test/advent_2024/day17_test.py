from unittest import TestCase

from main.advent_2024.day17 import part1, part2
from test.advent_2024 import get_input_test, get_input


class Day1Test(TestCase):
    def test_day17_part1_ex1(self):
        self.assertEqual("4,6,3,5,6,3,5,2,1,0", part1(get_input_test("day17")))

    def test_day17_part1(self):
        self.assertEqual("1,3,7,4,6,4,2,3,5", part1(get_input("day17")))

    def test_day17_part2_ex1(self):
        self.assertEqual(117440, part2(get_input_test("day17-1")))

    def test_day17_part2(self):
        self.assertEqual(202367025818154, part2(get_input("day17")))
