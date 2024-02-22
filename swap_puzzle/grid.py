"""
This is the grid module. It contains the Grid class and its associated methods.
"""
#import matplotlib.pyplot as plt
import random
from collections import deque
from graph import Graph
class Grid():
    """
    A class representing the grid from the swap puzzle. It supports rectangular grids. 

    Attributes: 
    -----------
    m: int
        Number of lines in the grid
    n: int
        Number of columns in the grid
    state: list[list[int]]
        The state of the grid, a list of list such that state[i][j] is the number in the cell (i, j), i.e., in the i-th line and j-th column. 
        Note: lines are numbered 0..m and columns are numbered 0..n.
    """
    
    def __init__(self, m, n, initial_state = []):
        """
        Initializes the grid.

        Parameters: 
        -----------
        m: int
            Number of lines in the grid
        n: int
            Number of columns in the grid
        initial_state: list[list[int]]
            The intiail state of the grid. Default is empty (then the grid is created sorted).
        """
        self.m = m
        self.n = n
        if not initial_state:
            initial_state = [list(range(i*n+1, (i+1)*n+1)) for i in range(m)]            
        self.state = initial_state

    def __str__(self): 
        """
        Prints the state of the grid as text.
        """
        output = f"The grid is in the following state:\n"
        for i in range(self.m): 
            output += f"{self.state[i]}\n"
        return output

    def __repr__(self): 
        """
        Returns a representation of the grid with number of rows and columns.
        """
        return f"<grid.Grid: m={self.m}, n={self.n}>"

   
    # Question 2
   
    def swap(self, cell1, cell2):
        """
        Implements the swap operation between two cells. Raises an exception if the swap is not allowed.

        Parameters: 
        -----------
        cell1, cell2: tuple[int]
            The two cells to swap. They must be in the format (i, j) where i is the line and j the column number of the cell. 
        """
        # we statrt by checking if the swap is allowed
        assert((cell1[0]==cell2[0] and abs(cell1[1]-cell2[1])==1) or (cell1[1]==cell2[1] and abs(cell1[0]-cell2[0])==1))
        # then we swap the two cells
        (a,b)=cell1
        (c,d)=cell2
        x=self.state[a][b]
        y=self.state[c][d]
        self.state[a][b]=y
        self.state[c][d]=x


    def swap_seq(self, cell_pair_list):
        
        """
        Executes a sequence of swaps. 

        Parameters: 
        -----------
        cell_pair_list: list[tuple[tuple[int]]]
            List of swaps, each swap being a tuple of two cells (each cell being a tuple of integers). 
            So the format should be [((i1, j1), (i2, j2)), ((i1', j1'), (i2', j2')), ...].
        """
        for i in range(len(cell_pair_list)):
            self.swap(cell_pair_list[i][0], cell_pair_list[i][1])
    #we use the previous function on all couples of cell given in cell_pair_list



    def is_sorted(self): #return "True" if the grid is sorted, "False" if it is not
        n = self.n
        m = self.m
        l = self.state
        for i in range(m):
            for j in range(n-1):
                if l[i][j] > l[i][j+1]:
                    return False
        return True
        

    
    #graphic representation
    def trace(self):
        _, ax = plt.subplots()

        ax.matshow(self.state, cmap=plt.cm.Blues)
        for i in range(self.n):
            for j in range(self.m):
                c = self.state[j][i]
                ax.text(i, j, str(c), va='center', ha='center')
        plt.show()


    #question 6
    def to_hashable(self): #return an hashable representation of a grid
        return (tuple(tuple(line) for line in self.state))
    
    @staticmethod
    def from_hashable(hashable_state:tuple): #return a grid from an hashable representation of a grid
        content= [list(row) for row in hashable_state]
        m=len(content)
        n=len(content[0])
        return(Grid(m,n,content))
   
    
    
    
    #question 7

    def neighbors(node): #return a list of all nods linked with the input node
        l=[]
        g=Grid.from_hashable(node)
        m=g.m
        n=g.n
    #we treat the last column and the last lign after the general case to prevent for index problems
        #for each cell in the grid(grid from node), we use swap with the cell on the right or on the bottom of it which gives two neighbors we add to the list of neighbors
        for i in range(m-1):
            for j in range(n-1):
                #swap to the right then return at the initial state (before the swap)
                g.swap((i,j),(i,j+1))
                l+=[Grid.to_hashable(g)]
                g.swap((i,j),(i,j+1))
                #swap to the bottom then return at the initial state(before the swap)
                g.swap((i,j),(i+1,j))
                l+=[Grid.to_hashable(g)]
                g.swap((i,j),(i+1,j))
                #g is unchanged  
        for j in range(n-1):
            g.swap((m-1,j),(m-1,j+1))
            l+=[Grid.to_hashable(g)]
            g.swap((m-1,j),(m-1,j+1))
        for i in range(m-1):
            g.swap((i,n-1),(i+1,n-1))
            l+=[Grid.to_hashable(g)]
            g.swap((i,n-1),(i+1,n-1))
        return(l)
    #such as the previous function we just have to do swaps with cells on the right or on the bottom
   

    
    def all_nodes(self):# we use a Breadth-First Search (BFS) to add to a list all nodes from a graph whom source is an input grid 
        initial_node=self.to_hashable()
        queue = [(initial_node, [initial_node])]
        visited=[]
        list_nodes=[]
        while queue: 
            node,path  = queue.pop(0)
            list_nodes+=[node]
            visited+=[node]
            for neighbor in Grid.neighbors(node):
                if neighbor not in visited:
                    queue.append((neighbor, path + [neighbor]))
        return(list_nodes)
                
                                  
        
    def edges(self):#return the list of all edges in the graph and the number of edges
        l=[]
        nb=0
        for x in Grid.all_nodes(self):
            for y in Grid.neighbors(x):
                l+=(x,y)
                nb+=1
        return(l,nb)

    def cplswap_from_edge(n1,n2):#return the couple of cells that have been swaped to get n2 from n1 or n1 from n2(we suppose that n2 is a neigbor of n1)
        """grid1=Grid.from_hashable(n1)
        grid2=Grid.from_hashable(n2)"""
        m=len(n1)
        n=len(n1[0])
        for i in range(m-1):
            for j in range(n-1):
                if n1[i][j] != n2[i][j]:
                    if n2[i][j+1]==n1[i][j] and n1[i][j+1]==n2[i][j]:
                        return(((i,j),(i,j+1)))
                    elif n2[i+1][j]==n1[i][j] and n1[i+1][j]==n2[i][j]:
                        return(((i,j),(i+1,j)))
        for i in range(m-1):
            if n1[i][n-1] != n2[i][n-1]:
                if n2[i][n-1]==n1[i+1][n-1] and n1[i][n-1]==n2[i+1][n-1]:
                    return((i,n-1),(i+1,n-1))
        for j in range(n-1):
            if n1[m-1][j]==n2[m-1,j+1] and n2[m-1][j]==n1[m-1,j+1]:
                if n2[m-1][j]==n1[m-1][j+1] and  n1[m-1][j]==n2[m-1][j+1]:
                    return((m-1,j),(m-1,j+1))
                    
                    
    
    def graph_from_grid(self):#the final function that return a graph from a grid
        newgraph=Graph(self.all_nodes())
        newgraph.nodes=self.all_nodes()
        dict={}
        for node in self.all_nodes():
            dict[node]=Grid.neighbors(node)
        newgraph.graph=dict
        newgraph.nb_edges=(self.edges())[1]
        newgraph.nb_nodes=len(self.all_nodes())
        newgraph.edges=(self.edges())[0]
        return(newgraph)
    
    
    def opti_solution1(self):#now we can use the bfs function that will find the shortest way between the initial state and the sorted state of a grid
        listswap=[]
        graph=self.graph_from_grid()
        sortedgrid=Grid(self.m,self.n,[list(range(i*((self.n)+1), (i+1)*((self.n)+1))) for i in range(self.m,1)])
        #print(Grid.to_hashable(sortedgrid) in self.all_nodes())
        l=Graph.bfs(self.graph_from_grid(),Grid.to_hashable(self),Grid.to_hashable(sortedgrid))
        for i in range(len(l)-1):
            n1=l[i]
            n2=l[i+1]
            listswap+=[(Grid.cplswap_from_edge(n1,n2))]
        return(listswap)

    
   


    @classmethod
    def grid_from_file(cls, file_name): 
        """
        Creates a grid object from class Grid, initialized with the information from the file file_name.
        
        Parameters: 
        -----------
        file_name: str
            Name of the file to load. The file must be of the format: 
            - first line contains "m n" 
            - next m lines contain n integers that represent the state of the corresponding cell

        Output: 
        -------
        grid: Grid
            The grid
        """
        with open(file_name, "r") as file:
            m, n = map(int, file.readline().split())
            initial_state = [[] for i_line in range(m)]
            for i_line in range(m):
                line_state = list(map(int, file.readline().split()))
                if len(line_state) != n: 
                    raise Exception("Format incorrect")
                initial_state[i_line] = line_state
            grid = Grid(m, n, initial_state)
        return grid


