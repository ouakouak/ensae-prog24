import sys 
sys.path.append("swap_puzzle/")

import unittest 
from grid import Grid

"""
This class tests our function grid_from_file by comparing the result of the function 
with the wanted grid for grid1. 
"""

class Test_GridLoading(unittest.TestCase):
    def test_grid1(self):
        g = Grid.grid_from_file("input/grid1.in")
        self.assertEqual(g.m, 4)
        self.assertEqual(g.n, 2)
        self.assertEqual(g.state, [[1, 2], [3, 4], [5, 6], [8, 7]])

if __name__ == '__main__':
    unittest.main()
