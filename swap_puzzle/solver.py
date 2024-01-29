from grid import Grid

class Solver(Grid): 

    def __init__(self,m,n,initial_state):
        self.m=m
        self.n=n
        self.state=initial_state
   

    def get_solution(self):
        l=[]
        tabref=[list(range(i*(self.n)+1, (i+1)*(self.n)+1)) for i in range(self.m)]
        for num in range(len(self.state)):
            iref=0
            jref=0
            for i in range(self.m):
              for j in range(self.n):  
                if tabref[i][j]==num:
                    (iref,jref)=(i,j)
            for i in range(self.m):
              for j in range(self.n):  
                if self.state[i][j]==num:
                    while j<self.n:
                        self.swap((i,j),(i,j+1))
                        l+=[((i,j),(i,j+1))]
                        j+=1
                    while i >=0 and i != iref :
                        self.swap((i,self.n),(i-1,self.n))
                        l+=[((i,self.n),(i-1,self.n))]
                        i-=1
                    while j>=0 and j != jref :
                        self.swap((iref,j),(iref,j-1))
                        j-=1
                        l+=[((iref,j),(iref,j-1))]
        return(l)


        """
        Solves the grid and returns the sequence of swaps at the format 
        [((i1, j1), (i2, j2)), ((i1', j1'), (i2', j2')), ...]. 
        """
        # TODO: implement this function (and remove the line "raise NotImplementedError").
        # NOTE: you can add other methods and subclasses as much as necessary. The only thing imposed is the format of the solution returned.
        

