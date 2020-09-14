# grille - OK
ligne_0 = [2,6,1,3,7,5,4,8,9]
ligne_1 = [8,7,3,2,9,4,5,1,6]
ligne_2 = [4,0,0,8,6,0,3,0,0]

ligne_3 = [0,4,0,0,0,8,0,0,1]
ligne_4 = [1,8,0,0,4,0,0,3,5]
ligne_5 = [9,0,0,6,0,0,0,4,0]

ligne_6 = [0,0,4,0,5,9,0,0,8]
ligne_7 = [0,0,6,1,0,0,9,0,0]
ligne_8 = [5,9,0,0,2,6,0,7,0]

grille = [ligne_0, ligne_1, ligne_2, ligne_3, ligne_4, ligne_5, ligne_6, ligne_7, ligne_8]


# fonction qui affiche correctement la grille - OK
def print_grille(grille):
        for i in range(len(grille)):
                if i % 3 == 0 and i != 0:
                        print('-----------------------')
                for j in range(len(grille[0])):
                        if j % 3 == 0 and j != 0:
                                print(" | ", end="")
                        if j == 8:
                                print(grille[i][j])
                        else:
                                print(str(grille[i][j]) + " " , end="")  

# fonction qui détecte les possibilités de nombre par case - OK
def possible(y,x,n):
        global grille
        for i in range(0,9):
                if grille[y][i] == n:
                        return False
        for i in range(0,9):
                if grille[i][x] == n:
                        return False
        x0 = (x//3)*3
        y0 = (y//3)*3
        for i in range(0,3):
                for j in range(0,3):
                        if grille[y0+i][x0+j] == n:
                                return False
        return True
        
# fonction de résolution - OK
def solve():
        global grille
        for y in range(9):
                for x in range(9):
                        if grille[y][x] == 0:
                                for n in range(1,10):
                                        if possible(y,x,n):
                                                grille[y][x] = n
                                                solve()        
                                                grille[y][x] = 0
                                return
        print_grille(grille)
                                                
solve()