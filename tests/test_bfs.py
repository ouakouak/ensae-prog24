# This will work if ran from the root folder ensae-prog24
import sys 
sys.path.append("swap_puzzle/")

import unittest 
from grid import Grid
from graph import Graph


class Test_BFS1(unittest.TestCase):
    def test_bfs1(self):
        g = Graph.graph_from_file("input/graph1.in")
        f=g.bfs(6,16)
        self.assertEqual(f,[6,19,16])

if __name__ == '__main__':
    unittest.main()



