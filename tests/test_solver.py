# This will work if ran from the root folder ensae-prog24
import sys 
sys.path.append("swap_puzzle/")

import unittest 
from grid import Grid
from solver import Solver

class Test_Solver(unittest.TestCase):
    def test_solver1(self):
        g = Grid.grid_from_file("input/grid1.in")
        f = Solver(g)
        matrice_swaps = f.get_solution()
        self.assertEqual(matrice_swaps, [((3, 0), (3, -1))])

if __name__ == '__main__':
    unittest.main()
