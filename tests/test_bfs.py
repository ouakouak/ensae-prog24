import sys 
sys.path.append("swap_puzzle/")

import unittest 
from grid import Grid
from graph import Graph

""" 
In this class, we check if our BFS function works for graphs 1 & 2. 
In each function, two integers are given and the BFS function returns the 
path between two integers. We check after if it is the wanted path
(thanks to the data given in the "path.out" files).
"""

class Test_BFS1(unittest.TestCase):
    def test_bfs1(self):
        g = Graph.graph_from_file("input/graph1.in")
        f=g.bfs(6,16)
        self.assertEqual(f,[6,19,16])

    def test_bfs2(self):
        g = Graph.graph_from_file("input/graph2.in")
        f=g.bfs(6,16)
        self.assertEqual(f,None)
        h=g.bfs(7,15)
        self.assertEqual(h,[7, 17, 18, 4, 15])

if __name__ == '__main__':
    unittest.main()

    