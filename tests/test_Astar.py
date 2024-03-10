import sys 
sys.path.append("swap_puzzle/")

import unittest 
from grid import Grid
from graph import Graph

""" 
In this class, we check if our AStar function works, trying it on all the grids given. 
 Each function works for a specific grid, wich number goes from 0 to 4. 
 For all grids, the function just checks if the swaps done to ordonate 
 the grid are the optimal ones (according to the Astar method). 
 """

class Test_Astar(unittest.TestCase):
    def test_Astar_0(self):
        g = Grid.grid_from_file("input/grid0.in")
        l=g.Astar()
        grid=Grid.from_hashable(l[-1])
        self.assertEqual(grid.state,[[1,2],[3,4]])
        self.assertEqual(Grid.noswaperror(l),'no swap error')
    
    def test_Astar_1(self):
        g = Grid.grid_from_file("input/grid1.in")
        l=g.Astar()
        grid=Grid.from_hashable(l[-1])
        self.assertEqual(grid.state,[[1,2],[3,4],[5,6],[7,8]])
        self.assertEqual(Grid.noswaperror(l),'no swap error')

    def test_Astar_2(self):
        g = Grid.grid_from_file("input/grid2.in")
        l=g.Astar()
        grid=Grid.from_hashable(l[-1])
        self.assertEqual(grid.state,[[1,2,3],[4,5,6],[7,8,9]])
        self.assertEqual(Grid.noswaperror(l),'no swap error')

    def test_Astar_3(self):
        g = Grid.grid_from_file("input/grid3.in")
        l=g.Astar()
        grid=Grid.from_hashable(l[-1])
        self.assertEqual(grid.state,[[1,2,3,4],[5,6,7,8],[9,10,11,12],[13,14,15,16]])
        self.assertEqual(Grid.noswaperror(l),'no swap error')

    def test_Astar_4(self):
        g = Grid.grid_from_file("input/grid4.in")
        l=g.Astar()
        grid=Grid.from_hashable(l[-1])
        self.assertEqual(grid.state,[[1,2,3,4],[5,6,7,8],[9,10,11,12],[13,14,15,16]])
        self.assertEqual(Grid.noswaperror(l),'no swap error')

if __name__ == '__main__':
    unittest.main() 
