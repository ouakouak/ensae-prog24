import sys 
sys.path.append("swap_puzzle/")

import unittest 
from grid import Grid
from solver import Solver

class Test_Solver(unittest.TestCase):
    def test_solver1(self):
        g = Grid.grid_from_file("input/grid1.in")
        f = Solver(g)
        f.get_solution()
        solution=(f.g).state
        self.assertEqual(solution, [[1,2],[3,4],[5,6],[7,8]])

if __name__ == '__main__':
    unittest.main()

    
