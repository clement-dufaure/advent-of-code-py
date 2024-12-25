from unittest import TestCase

from main.advent_2024.day18 import part1, part2
from test.advent_2024 import get_input_test, get_input


class Day1Test(TestCase):
    def test_day18_part1_ex1(self):
        self.assertEqual(22, part1(get_input_test("day18"), max_x=6, max_y=6, how_many_lines=12))

    def test_day18_part1(self):
        self.assertEqual(268, part1(get_input("day18")))

    def test_day18_part2_ex1(self):
        self.assertEqual("6,1", part2(get_input_test("day18"), max_x=6, max_y=6, start_i=13))

    # 22s
    # i=2934
    def test_day18_part2(self):
        self.assertEqual("64,11", part2(get_input("day18")))
