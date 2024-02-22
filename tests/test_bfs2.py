# This will work if ran from the root folder ensae-prog24
import sys 
sys.path.append("swap_puzzle/")

import unittest 
from grid import Grid
from graph import Graph


class Test_BFS2(unittest.TestCase):
    def test_bfs1(self):
        g = Graph.graph_from_file("input/graph2.in")
        f=g.bfs(6,16)
        self.assertEqual(f,None)
        h=g.bfs(7,15)
        self.assertEqual(h,[7, 17, 18, 4, 15])

if __name__ == '__main__':
    unittest.main()