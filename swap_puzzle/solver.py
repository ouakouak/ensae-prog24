from grid import Grid

class Solver(): # Question 3

    '''Pour chaque entier de la grille, dans un ordre croissant, on le déplace d'abord tout à droite, 
    puis aussi en haut qu'il est possible pour lui d'être,
    enfin on le positionne à ses bonnes coordonnées en
    le déplaçant à gauche autant qu'on peut.'''

    def __init__(self,grid):
        self.g=grid
   

    def get_solution(self):
        l=[]
        tabref=[list(range(i*((self.g).n)+1, (i+1)*((self.g).n)+1)) for i in range((self.g).m)]
        for num in range(1,(self.g).m*(self.g).n):
            iref=0
            jref=0
            for i in range((self.g).m):
              for j in range((self.g).n):  
                if tabref[i][j]==num:
                    (iref,jref)=(i,j)
            for i in range((self.g).m):
              for j in range((self.g).n):  
                if (self.g).state[i][j]==num:
                    while j<(self.g).n-1:
                        (self.g).swap((i,j),(i,j+1))
                        l+=[((i,j),(i,j+1))]
                        j+=1
                    print((self.g).state)
                    while i >=0 and i != iref :
                        (self.g).swap((i,(self.g).n-1),(i-1,(self.g).n-1))
                        l+=[((i,(self.g).n-1),(i-1,(self.g).n-1))]
                        i-=1
                    print((self.g).state)
                    while j>=0 and j != jref :
                        (self.g).swap((iref,j),(iref,j-1))
                        j-=1
                        l+=[((iref,j),(iref,j-1))]
                    print((self.g).state)
            print(num)
        return(l)


        """
        Solves the grid and returns the sequence of swaps at the format 
        [((i1, j1), (i2, j2)), ((i1', j1'), (i2', j2')), ...]. 
        """
        # TODO: implement this function (and remove the line "raise NotImplementedError").
        # NOTE: you can add other methods and subclasses as much as necessary. The only thing imposed is the format of the solution returned.
        

