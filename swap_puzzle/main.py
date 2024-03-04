from grid import Grid
from solver import Solver
from graph import Graph
g=Grid(2,3,[[1,3,2],[5,4,6]])


grid1 = Grid.grid_from_file("input/grid1.in")
print(grid1.opti_solution1())





'''
data_path = "../input/"
file_name = data_path + "grid0.in"

print(file_name)

g = Grid.grid_from_file(file_name)
print(g)
'''


