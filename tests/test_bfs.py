# This will work if ran from the root folder ensae-prog24
import sys 
sys.path.append("swap_puzzle/")

import unittest 
from grid import Grid
from graph import Graph

class Test_BFS(unittest.TestCase):
    def test_bfs1(self):
        g = Graph.graph_from_file("/workspaces/ensae-prog24/input/graph1.in")
        for i in range(1,20,1) :
            for j in range(1,20,1) :
                f = g.bfs(i,j)
                for a in "/workspaces/ensae-prog24/input/graph1.path.out" : #doute : parcourt-on bien toutes les lignes ? 
                    if a[0:4] == str(i)+" "+str(j) :
                        b = a[8: -1]
                        self.assertEqual(f, b)
                    elif a[0:3] == str(i)+" "+str(j) :
                        b = a[7:-1]
                        self.assertEqual(f, b)

if __name__ == '__main__':
    unittest.main()
