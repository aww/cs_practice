#!/usr/bin/env python

import unittest

# Definition for a point
class Point:
    def __init__(self, a=0, b=0):
        self.x = a
        self.y = b

class Solution:
    def gcd(self, a, b):
        """Greatest common divisor, where the special cases are
        (0,0)->1, (a,0)->a, (0,b)->b,
        and otherwise the GCD returned is given the same sign as b."""
        if a==0:
            if b==0:
                return 1
            else:
                return b
        elif b==0:
            return a
        else:
            neg = (b < 0) # we'll give gcd
            a = abs(a)
            b = abs(b)
            r0 = (a if a > b else b)
            r1 = (b if a > b else a)
            while r1 != 0:
                r2 = r0 % r1
                r0 = r1
                r1 = r2
            return (-r0 if neg else r0)

    # @param points, a list of Points
    # @return an integer
    def maxPoints(self, points):
        N = len(points)
        if N < 3:
            return N
        max_points = 2
        # For every unordered pair of points p1, p2 count how many other points p3
        # are on the line defined by p1 and p2.
        # Equation of the line is (y - y1)(x2 - x1) = (x-x1)(x2-x1)
        for i in range(N):
            p0 = points[i]
            slopes = {}
            max_in_slopes = 0
            n_duplicates = 1
            for j in range(i+1, N):
                dy,dx = points[j].y - p0.y, points[j].x - p0.x
                g = self.gcd(dy,dx)
                dydx = (dy/g, dx/g) # now relatively prime and dx >= 0
                if dydx == (0,0):
                    n_duplicates += 1
                else:
                    if dydx in slopes:
                        slopes[dydx] += 1
                    else:
                        slopes[dydx] = 1
                    if slopes[dydx] > max_in_slopes:
                        max_in_slopes = slopes[dydx]
            max_points = max(n_duplicates + max_in_slopes, max_points)
            # for j in range(i+1, N):
            #     n_points_this_line = 2
            #     dx = (points[j].x-points[i].x)
            #     dy = (points[j].y-points[i].y)
            #     for k in range(j+1, N):
            #         if ((points[k].y-points[i].y)*dx == (points[k].x-points[i].x)*dy):
            #             n_points_this_line += 1
            #     max_points = max(n_points_this_line, max_points)
        return max_points

class TestGCD(unittest.TestCase):
    def setUp(self):
        self.sol = Solution()
    def test_axis(self):
        self.assertEqual(self.sol.gcd(1,0), 1)
        self.assertEqual(self.sol.gcd(-1,0), -1)
        self.assertEqual(self.sol.gcd(-4,0), -4)
        self.assertEqual(self.sol.gcd(0,4), 4)
        self.assertEqual(self.sol.gcd(0,1), 1)
        self.assertEqual(self.sol.gcd(0,-1), -1)
        self.assertEqual(self.sol.gcd(0,-4), -4)
    def test_sign(self):
        self.assertEqual(self.sol.gcd( 4, 6),  2)
        self.assertEqual(self.sol.gcd(-4, 6),  2)
        self.assertEqual(self.sol.gcd( 4,-6), -2)
        self.assertEqual(self.sol.gcd(-4,-6), -2)
    def test_complex(self):
        self.assertEqual(self.sol.gcd(2*3*4*5,2*3*7*11), 2*3)
        self.assertEqual(self.sol.gcd(2*3*5*7*9*11*11*13*13,11*11*11*13*13*13), 11*11*13*13)
        self.assertEqual(self.sol.gcd(2**10,2**6), 2**6)
        self.assertEqual(self.sol.gcd(2**6,2**10), 2**6)

class TestMaxPoints(unittest.TestCase):
    def setUp(self):
        self.sol = Solution()

    def test_empty(self):
        self.assertEqual(self.sol.maxPoints([]), 0)

    def test_one(self):
        self.assertEqual(self.sol.maxPoints([Point(1,2)]), 1)

    def test_two(self):
        self.assertEqual(self.sol.maxPoints([Point(1,2), Point(3,4)]), 2)

    def test_duplicates(self):
        self.assertEqual(self.sol.maxPoints([Point(1,1), Point(1,1)]), 2)
        self.assertEqual(self.sol.maxPoints([Point(0,0), Point(1,1), Point(0,0)]), 3)
        self.assertEqual(self.sol.maxPoints([Point(0,0), Point(1,1), Point(1,1), Point(0,0)]), 4)

    def test_threetri(self):
        self.assertEqual(self.sol.maxPoints([Point(1,0), Point(-1,0), Point(0,1)]), 2)

    def test_threeline(self):
        self.assertEqual(self.sol.maxPoints([Point(1,2), Point(2,4), Point(4,8)]), 3)

    def test_fourthree(self):
        self.assertEqual(self.sol.maxPoints([Point(1,2), Point(2,4), Point(4,8), Point(1,0)]), 3)

    def test_huge(self):
        points = map(lambda x: Point(x[0],x[1]), [(29,87),(145,227),(400,84),(800,179),(60,950),(560,122),(-6,5),(-87,-53),(-64,-118),(-204,-388),(720,160),(-232,-228),(-72,-135),(-102,-163),(-68,-88),(-116,-95),(-34,-13),(170,437),(40,103),(0,-38),(-10,-7),(-36,-114),(238,587),(-340,-140),(-7,2),(36,586),(60,950),(-42,-597),(-4,-6),(0,18),(36,586),(18,0),(-720,-182),(240,46),(5,-6),(261,367),(-203,-193),(240,46),(400,84),(72,114),(0,62),(-42,-597),(-170,-76),(-174,-158),(68,212),(-480,-125),(5,-6),(0,-38),(174,262),(34,137),(-232,-187),(-232,-228),(232,332),(-64,-118),(-240,-68),(272,662),(-40,-67),(203,158),(-203,-164),(272,662),(56,137),(4,-1),(-18,-233),(240,46),(-3,2),(640,141),(-480,-125),(-29,17),(-64,-118),(800,179),(-56,-101),(36,586),(-64,-118),(-87,-53),(-29,17),(320,65),(7,5),(40,103),(136,362),(-320,-87),(-5,5),(-340,-688),(-232,-228),(9,1),(-27,-95),(7,-5),(58,122),(48,120),(8,35),(-272,-538),(34,137),(-800,-201),(-68,-88),(29,87),(160,27),(72,171),(261,367),(-56,-101),(-9,-2),(0,52),(-6,-7),(170,437),(-261,-210),(-48,-84),(-63,-171),(-24,-33),(-68,-88),(-204,-388),(40,103),(34,137),(-204,-388),(-400,-106)])
        self.assertEqual(self.sol.maxPoints(points), 21)

if __name__ == "__main__":
    unittest.main()
