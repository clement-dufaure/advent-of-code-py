from unittest import TestCase

from main.advent_2024.day24 import part1, part2
from test.advent_2024 import get_input_test, get_input


class Day1Test(TestCase):
    def test_day24_part1_ex1(self):
        self.assertEqual(4, part1(get_input_test("day24")))

    def test_day24_part1_ex2(self):
        self.assertEqual(2024, part1(get_input_test("day24-1")))

    def test_day24_part1(self):
        self.assertEqual(57344080719736, part1(get_input("day24")))

    def test_day24_part2(self):
        self.assertEqual("cgq,fnr,kqk,nbc,svm,z15,z23,z39", part2(get_input("day24")))
