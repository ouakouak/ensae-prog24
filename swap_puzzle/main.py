from grid import Grid
from solver import Solver
from graph import Graph
carla=[[5,3,6],[2,1,4]]
g = Grid(2, 3, carla)
g.swap((0,0),(0,1))
#print(g)
S=Solver(g)
#print(S.get_solution())
#print(g)

graph1 = Graph.graph_from_file("/workspaces/ensae-prog24/input/graph1.in")
print(graph1.bfs(1,7))

'''
data_path = "../input/"
file_name = data_path + "grid0.in"

print(file_name)

g = Grid.grid_from_file(file_name)
print(g)
'''


