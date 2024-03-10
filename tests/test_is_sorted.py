import sys 
sys.path.append("swap_puzzle/")

import unittest 
from grid import Grid

"""
This class tests our function Is_Sorted by first checking if the function returns a False 
for an unordered grid, then by checking if the function returns a True once the right swap is 
done to order the grid. 
"""

class Test_Is_Sorted(unittest.TestCase):
    def test_grid1(self):
        grid = Grid.grid_from_file("input/grid1.in")
        self.assertEqual(grid.is_sorted(), False)
        grid.swap((3,0), (3,1))
        self.assertEqual(grid.is_sorted(), True)

if __name__ == '__main__':
    unittest.main()