"""
This is the grid module. It contains the Grid class and its associated methods.
"""
import matplotlib.pyplot as plt 
import random
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
        # On commence par vérifier que le swap est possible
        assert((cell1[0]==cell2[0] and abs(cell1[1]-cell2[1])==1) or (cell1[1]==cell2[1] and abs(cell1[0]-cell2[0])==1))
        # puis on l'effectue
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
    '''On utilise la fonction swap préalablement définie qu'on éxecute sur les couples de cellules fournis dans 
    la liste de cellules à échanger(celle_pair_list)'''
        
    def is_sorted(self): #On vérifie dans cette fonction que les cellules sont rangées par ordre croissant
        n = self.n
        m = self.m
        l = self.state
        for i in range(m):
            for j in range(n-1):
                if l[i][j] > l[i][j+1]:
                    return False
        return True
        """
        Checks is the current state of the grid is sorte and returns the answer as a boolean.
        """ 

    
    #Représentation graphique
    def trace(self):
        _, ax = plt.subplots()

        ax.matshow(self.state, cmap=plt.cm.Blues)
        for i in range(self.n):
            for j in range(self.m):
                c = self.state[j][i]
                ax.text(i, j, str(c), va='center', ha='center')
        plt.show()


    #question 6
    def to_hashable(self): #retourne une représentation hashable de la grille
        return (tuple(tuple(line) for line in self.state))
    
    @staticmethod
    def from_hashable(hashable_state:tuple): #retourne une grille depuis une version hashable de grille 
        content= [list(row) for row in hashable_state]
        m=len(content)
        n=len(content[0])
        return(Grid(m,n,content))
    
    def n1n2edge(n1,n2):#création d'arête entre deux noeuds (qu'on suppose de même format)
        compteur=0
        diff_sans_swap=0
        g1=Grid.from_hashable(n1)
        g2=Grid.from_hashable(n2)
        m=g1.m
        n=g1.n
        #on vérifie qu'il existe un unique swap permettant de passer de g1 à g2 
        #on sépare les cas selon qu'on se trouve sur la dernière colonne ou la dernière ligne 
        for i in range(m-1):
            for j in range(n-1):
                if g1[i][j] != g2[i][j]:
                    if g2[i][j+1]==g1[i][j] and g1[i][j+1]==g2[i][j]:
                        compteur+=1
                    elif g2[i+1][j]==g1[i][j] and g1[i+1][j]==g2[i][j]:
                        compteur+=1
                    else:
                        diff_sans_swap+=1
        for i in range(m-1):
            if g2[i][n-1]==g1[i+1][n-1] and g1[i][n-1]==g2[i+1][n-1]:
                compteur+=1
        for j in range(n-1):
            if g2[m-1][j]==g1[m-1][j+1] and  g1[m-1][j]==g2[m-1][j+1]:
                compteur+=1
        if compteur==1 and diff_sans_swap==0:
            return((n1,n2))
        
    def voisins(node): #on créer la liste de tous les noeuds reliés à un noeud quelconque
        l=[]
        g=Grid.from_hashable(node)
        m=g.m
        n=g.n
        #de même on sépare les cas de la dernière ligne et dernière colonne 
        for i in range(m-1):
            for j in range(n-1):
                g1=g.state
                g2=g.state
                g1.swap((i,j),(i,j+1))
                g2.swap((i,j),(i+1,j))
                l+=[Grid.to_hashable(g1)]+[Grid.to_hashable(g2)]
        for j in range(n-1):
            g1=g.state
            g1.swap((m-1,j),(m-1,j+1))
            l+=[Grid.to_hashable(g1)]
        for i in range(m-1):
            g2=g.state
            g2.swap((i,n-1),(i+1,n-1))
            l+=[Grid.to_hashable(g2)]
        return(l)
    
   

    def auxi(grid,l):
        m=0
        for x in Grid.voisins(Grid.to_hashable(grid)):
            if x in l:
                m+=1
        if m==len(Grid.voisins(Grid.to_hashable(grid))):
            l+=[]
        else :
            for x in Grid.voisins(Grid.to_hashable(grid)):
                if x not in l:
                    l+=[x]+Grid.auxi(Grid.from_hashable(x))
                    
            

    def tous_les_noeuds(self):
        l=[]
        l+=Grid.auxi(self.state,l)
        return(l)
        
    def arêtes(self):
        l=[]
        nb=0
        for x in Grid.tous_les_noeuds():
            for y in Grid.voisins(x):
                l+=Grid.n1n2edge(x,y)
                nb+=1
        return(l,nb)
        
            
                
    
    def graph_from_grid(self):
        dict={}
        for x in self.tous_les_noeuds():
            dict[x]=Grid.voisins(x)
        return(Graph(self.tous_les_noeuds,dict,len(self.tous_les_noeuds),(self.arêtes())[1],(self.arêtes())[0]))
    
    def solution_optimale1(self):
        graph=self.graph_from_grid()
        return (self.bfs(Grid.to_hashable(self.state),Grid.to_hashable(tabref=[list(range(i*((self.g).n)+1, (i+1)*((self.g).n)+1)) for i in range((self.g).m)])))


                    
                

                


        

        
                        
        

    
    #question 7


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


