import sys 
sys.path.append("swap_puzzle/")

import unittest 
from grid import Grid
from graph import Graph


"""

"""

class Test_neighbors(unittest.TestCase):
    def test_neighbors0(self):
        g = Grid.grid_from_file("input/grid0.in")
        f=Grid.neighbors(Grid.to_hashable(g))
        self.assertEqual(f,[((4,2),(3,1)),((3,4),(2,1)),((2,4),(1,3)),((2,1),(3,4))])
    
if __name__ == '__main__':
    unittest.main()

    