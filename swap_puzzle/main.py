from grid import Grid
from solver import Solver
from graph import Graph
import random as rd
import pygame
import sys

# Initialisation de Pygame
pygame.init()

# Définition des couleurs
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)

# Définition de la taille de la fenêtre
WINDOW_WIDTH = 600
WINDOW_HEIGHT = 600

# Création de la fenêtre
window = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
pygame.display.set_caption("ouakileur's game")

# définition des paramètres de la grille
m=6
n=6 

# définition de la grille à résoudre
content=[list(range(i*(n)+1, (i+1)*(n)+1)) for i in range(m)]
print(content)
nbr_of_change=rd.randint(15,20)
new_content=content
for p in range(nbr_of_change):
    i,j=(rd.randint(0,m-1),rd.randint(0,n-1))
    print(i,j)
    # on considère les 4 coins 
    if (i,j)==(0,0):
        rido=rd.randint(0,1)#on choisit de manière random si on effectue un swap vers  la droite(ri) ou le bas(do)

        if rido==0:#swap vers la droite
            a=new_content[i][j]
            new_content[i][j]=new_content[i][j+1]
            new_content[i][j+1]=a
        
        if rido==1:#swap vers le bas
            a=new_content[i][j]
            new_content[i][j]=new_content[i+1][j]
            new_content[i+1][j]=a
        
    elif (i,j)==(0,n-1):
        ld=rd.randint(0,1)#on choisit de manière random si on effectue un swap vers la gauche(l) ou le bas(d)

        if ld==0:#swap vers la gauche
            a=new_content[i][j]
            new_content[i][j]=new_content[i][j-1]
            new_content[i][j-1]=a
        
        if ld==1:#swap vers le bas
            a=new_content[i][j]
            new_content[i][j]=new_content[i+1][j]
            new_content[i+1][j]=a 

    elif (i,j)==(m-1,0):
        ru=rd.randint(0,1)#on choisit de manière random si on effectue un swap vers la droite(r) ou le haut(u)

        
        if ru==0:#swap vers la droite
            a=new_content[i][j]
            new_content[i][j]=new_content[i][j+1]
            new_content[i][j+1]=a
        
        if ru==1:#swap vers le haut
            a=new_content[i][j]
            new_content[i][j]=new_content[i-1][j]
            new_content[i-1][j]=a
        
    elif (i,j)==(m-1,n-1):
        lu=rd.randint(0,1)#on choisit de manière random si on effectue un swap vers la gauche(l) ou le haut(u)

        if lu==0:#swap vers la gauche
            a=new_content[i][j]
            new_content[i][j]=new_content[i][j-1]
            new_content[i][j-1]=a
        
        if lu==1:#swap vers le haut
            a=new_content[i][j]
            new_content[i][j]=new_content[i-1][j]
            new_content[i-1][j]=a
    
    elif (i==0 and j!=0) or (i==0 and j!= n-1):#première ligne sans les coins
        lrd=rd.randint(1,3)#on choisit de manière random si on effectue un swap vers la gauche(l), la droite(r) ou le bas(d)

        if lrd==1:#swap vers la gauche
            a=new_content[i][j]
            new_content[i][j]=new_content[i][j-1]
            new_content[i][j-1]=a

        if lrd==2:#swap vers la droite
            a=new_content[i][j]
            new_content[i][j]=new_content[i][j+1]
            new_content[i][j+1]=a
        
        if lrd==4:#swap vers le bas
            a=new_content[i][j]
            new_content[i][j]=new_content[i+1][j]
            new_content[i+1][j]=a

    elif (i==m-1 and j!=0)  or (i==m-1 and j!= n-1):#dernière ligne sans les coins
        lru=rd.randint(1,3)#on choisit de manière random si on effectue un swap vers la gauche(l), la droite(r) ou le haut(u)

        if lru==1:#swap vers la gauche
            a=new_content[i][j]
            new_content[i][j]=new_content[i][j-1]
            new_content[i][j-1]=a

        if lru==2:#swap vers la droite
            a=new_content[i][j]
            new_content[i][j]=new_content[i][j+1]
            new_content[i][j+1]=a
        
        if lru==4:#swap vers le haut
            a=new_content[i][j]
            new_content[i][j]=new_content[i-1][j]
            new_content[i-1][j]=a
        
    elif (i!=m-1 and j==0) or (i!=0 and j==0):#première colonne sans les coins
        rud=rd.randint(1,3)#on choisit de manière random si on effectue un swap vers la droite(r), le haut(u) ou le bas(d)


        if rud==1:#swap vers la droite
            a=new_content[i][j]
            new_content[i][j]=new_content[i][j+1]
            new_content[i][j+1]=a
        
        if rud==2:#swap vers le haut
            a=new_content[i][j]
            new_content[i][j]=new_content[i-1][j]
            new_content[i-1][j]=a

        if rud==3:#swap vers le bas
            a=new_content[i][j]
            new_content[i][j]=new_content[i+1][j]
            new_content[i+1][j]=a
        
    elif (i!=m-1 and j==0) or (i!=0 and j==0):#dernière colonne sans les coins
        lud=rd.randint(1,3)#on choisit de manière random si on effectue un swap vers la gauche(l), le haut(u) ou le bas(d)

        if lud==1:#swap vers la gauche
            a=new_content[i][j]
            new_content[i][j]=new_content[i][j-1]
            new_content[i][j-1]=a
        
        if lud==2:#swap vers le haut
            a=new_content[i][j]
            new_content[i][j]=new_content[i-1][j]
            new_content[i-1][j]=a

        if lud==3:#swap vers le bas
            a=new_content[i][j]
            new_content[i][j]=new_content[i+1][j]
            new_content[i+1][j]=a


    elif i!=0 and j!=0 and i!=m-1 and j!=n-1:# on considére toutes les cellules intérieures a la grille
        
        lrud=rd.randint(1,4)#on choisit de manière random si on effectue un swap vers la gauche(l), la droite(r), le haut(u) ou le bas(d)
        
        if lrud==1:#swap vers la gauche
            a=new_content[i][j]
            new_content[i][j]=new_content[i][j-1]
            new_content[i][j-1]=a

        if lrud==2:#swap vers la droite
            a=new_content[i][j]
            new_content[i][j]=new_content[i][j+1]
            new_content[i][j+1]=a
        
        if lrud==3:#swap vers le haut
            a=new_content[i][j]
            new_content[i][j]=new_content[i-1][j]
            new_content[i-1][j]=a
        
        if lrud==4:#swap vers le bas
            a=new_content[i][j]
            new_content[i][j]=new_content[i+1][j]
            new_content[i+1][j]=a
        
    

#dessiner la grille
            
CELL_SIZE = WINDOW_WIDTH // m
# Fonction pour dessiner la grille
def draw_grid():
    for i in range(m):
        for j in range(n):
            pygame.draw.rect(window, WHITE, (i * CELL_SIZE, j * CELL_SIZE, CELL_SIZE, CELL_SIZE), 1)

def draw_numbers(numbers):
    font = pygame.font.SysFont(None, 40)
    for i in range(m):
        for j in range(n):
            text = font.render(str(numbers[i][j]), True, WHITE)
            text_rect = text.get_rect(center=(i * CELL_SIZE + CELL_SIZE // 2, j * CELL_SIZE + CELL_SIZE // 2))
            window.blit(text, text_rect)




# Boucle principale du jeu
numbers=new_content

running = True
selected_cell = None
while running:
    # Gestion des événements
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.MOUSEBUTTONDOWN:
            mouse_pos = pygame.mouse.get_pos()
            cell_x = mouse_pos[0] // CELL_SIZE
            cell_y = mouse_pos[1] // CELL_SIZE
            selected_cell = (cell_x, cell_y)
     # Effacer l'écran
    window.fill(BLACK)
    draw_grid()
    draw_numbers(numbers)
    
    # Dessiner la cellule sélectionnée en gras
    if selected_cell is not None:
        cell_rect = pygame.Rect(selected_cell[0] * CELL_SIZE, selected_cell[1] * CELL_SIZE, CELL_SIZE, CELL_SIZE)
    
        pygame.draw.rect(window, RED, cell_rect, 3)
    
   

    
    

    # Mettre à jour l'affichage
    pygame.display.update()

    # Limiter le taux de rafraîchissement de l'écran
    pygame.time.Clock().tick(30)

# Quitter Pygame
pygame.quit()
sys.exit()







'''
data_path = "../input/"
file_name = data_path + "grid0.in"

print(file_name)

g = Grid.grid_from_file(file_name)
print(g)
'''


