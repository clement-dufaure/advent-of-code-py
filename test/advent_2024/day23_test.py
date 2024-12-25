from unittest import TestCase

from main.advent_2024.day23 import part1, part2
from test.advent_2024 import get_input_test, get_input


class Day1Test(TestCase):
    def test_day23_part1_ex1(self):
        self.assertEqual(7, part1(get_input_test("day23")))

    def test_day23_part1(self):
        self.assertEqual(1043, part1(get_input("day23")))

    def test_day23_part2_ex1(self):
        self.assertEqual("co,de,ka,ta", part2(get_input_test("day23")))

    # 8s
    def test_day23_part2(self):
        self.assertEqual("ai,bk,dc,dx,fo,gx,hk,kd,os,uz,xn,yk,zs", part2(get_input("day23")))
