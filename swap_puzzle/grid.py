"""
This is the grid module. It contains the Grid class and its associated methods.
"""
import matplotlib.pyplot as plt
import numpy
import random


from graph import Graph
import heapq
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
    #we just have to do swaps with cells on the right or on the bottom
   
    """ 
    Let's denote the dimensions of the grid as m*n.

    Here's the breakdown of the complexity:
    The function iterates over each cell in the grid, which requires O(m*n) iterations.

    For each cell, it performs up to two swaps to generate neighboring configurations. 
    Swapping involves updating the positions of elements in the grid, which typically takes constant time.

    Thus, the total time complexity of the neighbors function is O(m*n).
    """
    


    def all_nodes(self):
        m=self.m
        n=self.n
        list_nodes=[]
        import itertools
        nums=[]
        for i in range(m*n):
            nums+=[i+1]
        permutations=tuple(itertools.permutations(nums))
        for x in permutations:
            i=0
            lignes=[]
            while i<=m*n-n+1:
                lignes+=[x[i:i+n]]
                i+=n
            list_nodes+=[tuple(lignes)]
        return(list_nodes)

    """
    Let's denote the dimensions of the grid as m*n.
    Here's the breakdown of the complexity:

    The function generates all permutations of numbers from 1 to m*n, which requires O((m*n)!) permutations in the worst case.
   
    For each permutation, the function constructs a grid representation, which involves reshaping the permutation into a m*n table. 
    This operation typically takes linear time, O(m*n), since it requires iterating over each element in the permutation.
    Thus, the total time complexity of the all_nodes function is dominated by the generation of permutations, and it is O((m*n)!*m*n).
    """                 
        
    def edges(self):#return the list of all edges in the graph and the number of edges
        l=[]
        nb=0
        for x in Grid.all_nodes(self):
            for y in Grid.neighbors(x):
                l+=(x,y)
                nb+=1
        return(l,nb)

    """the complexity is the complexity of all_nodes * the complexity of neighbors (in the worst case).
    Thus its O((m*n)!*(m*n))"""
    
    def cplswap_from_edge(n1,n2):#return the couple of cells that have been swaped to get n2 from n1 or n1 from n2(we suppose that n2 is a neigbor of n1)
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
            if n1[m-1][j]==n2[m-1][j+1] and n2[m-1][j]==n1[m-1][j+1]:
                if n2[m-1][j]==n1[m-1][j+1] and  n1[m-1][j]==n2[m-1][j+1]:
                    return((m-1,j),(m-1,j+1))

    """the total time complexity of the cplswap_from_edge function is O(m*n)."""             
                    
    
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
    """the time complexity of the graph_from_grid function is dominated by the generation of
      all nodes and finding their neighbors, which is neighbors_per_node O((m*n)!*m*n)"""
    
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

    """the total complexity of the opti_solution1 function is dominated by the complexity of graph 
    generation and execution of the BFS algorithm, which is of the order of neighbors_per_node
O((m*n)!*m*n"""


    
   # question 8 
    """To create an optimal version to find the shortest way between the input grid and the sorted grid,
       we choose to generates a smaller graph in a bfs way: we use a bfs method to generate the nodes until we get to the solution. 
       Thanks to that we will not generate a part of a graph that is not necessary to solve the problem which optimise 
       the time and the space.
       Then, we use the bfs function in the optimised graph to solve the problem.
       
       PS: It can be noticed that we could have use only one bfs to create the nodes and save the path in the same time but the complexity
       would have been the same within one factor
       """
    def all_nodes_opti(self):
        initial_node = self.to_hashable()
        sortedgrid = Grid(self.m, self.n, [list(range(i * ((self.n) + 1), (i + 1) * ((self.n) + 1))) for i in range(self.m, 1)])
        final_node = Grid.to_hashable(sortedgrid)
    
        queue = [initial_node]
        visited = []
    
        while queue:
            node = queue.pop(0)
            visited.append(node)
        
            if node == final_node:
                break
        
            for neighbor in Grid.neighbors(node):
                if neighbor not in visited:
                    queue.append(neighbor)
    
        return visited

     
    def edges_opti(self):#return the list of all edges in the graph and the number of edges
        l=[]
        nb=0
        for x in Grid.all_nodes_opti(self):
            for y in Grid.neighbors(x):
                l+=(x,y)
                nb+=1
        return(l,nb)

    def graph_from_grid_opti(self):#the final function that return a graph from a grid
        newgraph=Graph(self.all_nodes_opti())
        newgraph.nodes=self.all_nodes_opti()
        dict={}
        for node in self.all_nodes_opti():
            dict[node]=Grid.neighbors(node)
        newgraph.graph=dict
        newgraph.nb_edges=(self.edges_opti())[1]
        newgraph.nb_nodes=len(self.all_nodes_opti())
        newgraph.edges=(self.edges_opti())[0]
        return(newgraph)

    def opti_solution1_opti(self):#now we can use the bfs function that will find the shortest way between the initial state and the sorted state of a grid
        listswap=[]
        graph=self.graph_from_grid_opti()
        sortedgrid=Grid(self.m,self.n,[list(range(i*(self.n)+1, (i+1)*(self.n)+1)) for i in range(self.m)])
        #print(Grid.to_hashable(sortedgrid) in self.all_nodes())
        l=Graph.bfs(graph,Grid.to_hashable(self),Grid.to_hashable(sortedgrid))
        for i in range(len(l)-1):
            n1=l[i]
            n2=l[i+1]
            listswap+=[(Grid.cplswap_from_edge(n1,n2))]
        return(listswap) 
    
   
   
   
    #implémentation de A*

    
    #We firstly need to define an heuristic 
    
    def heuristic(node, goal):
        m=len(node)
        n=len(node[0])
        compteur=0
        for i in range(m):
            for j in range(n):
                if node[i][j]!=goal[i][j]:
                    compteur+=1
        return (compteur)
    
    def Astar(self):
        initial_node=self.to_hashable()
        sortedgrid=Grid(self.m,self.n,[list(range(i*((self.n)+1), (i+1)*((self.n)+1))) for i in range(self.m,1)])
        final_node=sortedgrid.to_hashable()
        
        queue=[((0,Grid.heuristic(initial_node,final_node)),initial_node)]
        path=[]

        while queue:
            (num,score),node = heapq.heappop(queue)
            path.append(node)
            print((num,score),node)

            if node==final_node:
                return(path)
            
            for x in Grid.neighbors(node):
                if x not in path:
                    scorex=Grid.heuristic(x,final_node)
                    heapq.heappush(queue,((num-1, scorex), x))
        
        
    def noswaperror(l):
        for i in range(len(l)-1):
            if l[i+1] not in Grid.neighbors(l[i]):
                return('swap error')
        return('no swap error')           

            

            








    


    


    


