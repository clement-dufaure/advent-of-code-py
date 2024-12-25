from unittest import TestCase

from main.advent_2024.day20 import part1, part2
from test.advent_2024 import get_input_test, get_input


class Day1Test(TestCase):
    def test_day20_part1_ex1(self):
        self.assertEqual(44, part1(get_input_test("day20"), min_raccourci=1))

    def test_day20_part1(self):
        self.assertEqual(1530, part1(get_input("day20")))

    def test_day20_part2_ex_back(self):
        self.assertEqual(44, part2(get_input_test("day20"), min_raccourci=1, picoseconds_cheat=2))

    def test_day20_part2_ex1(self):
        self.assertEqual(285, part2(get_input_test("day20"), min_raccourci=50, picoseconds_cheat=20))

    # 27s
    def test_day20_part2(self):
        self.assertEqual(1033983, part2(get_input("day20")))
