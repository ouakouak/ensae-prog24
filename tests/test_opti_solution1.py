import sys 
sys.path.append("swap_puzzle/")

import unittest 
from grid import Grid
from graph import Graph

class Test_optisolution1(unittest.TestCase):
    def test_optisolution1_0(self):
        g = Grid.grid_from_file("input/grid0.in")
        f=g.opti_solution1()
        g.swap_seq(f)
        self.assertEqual(g.state,[[1,2],[3,4]])
    
    def test_optisolution1_1(self):
        g = Grid.grid_from_file("input/grid1.in")
        f=g.opti_solution1()
        g.swap_seq(f)
        self.assertEqual(g.state,[[1,2],[3,4],[5,6],[7,8]])

if __name__ == '__main__':
    unittest.main()