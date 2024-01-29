from grid import Grid
from solver import Solver
carla=[[5,3,6],[2,1,4]]
g = Grid(2, 3, carla)
print(g)

'''
data_path = "../input/"
file_name = data_path + "grid0.in"

print(file_name)

g = Grid.grid_from_file(file_name)
print(g)
'''
carlasolver=Solver(2, 3, carla)
Solver.get_solution(carlasolver)
