# wolfram alpha
#plot x^2+y^2 = 16, (x-4)^2+(y-4)^2 =5

#guess: x=1.5 y=3
#guess: x=3.5 y=1.8

def f1(x,y):
    return (x - 4)**2 + (y-4)**2 -5

def f1xdiff(x,y):
    return 2*(x-4)

def f2xdiff(x,y):
    return 2*x

def f1ydiff(x,y):
    return 2*(y-4)

def f2ydiff(x,y):
    return 2*y

def j(x,y):
    return f1xdiff(x,y) * f2ydiff(x,y) - f1ydiff(x,y) *f2xdiff(x,y)
    
def f2(x,y):
    return x**2 + y**2 -16

def k(x,y):
    return -((f1xdiff(x,y) * f2(x,y)) - (f2xdiff(x,y) * f1(x,y)))/j(x,y)   
    
def h(x,y):
    return -((f1(x,y) * f2ydiff(x,y)) - (f2(x,y) * f1ydiff(x,y)))/j(x,y)


def newtonSistemas(x,y):
    
    for i in range(30):
        x1 = x + h(x,y)
        y1 = y + k(x,y)
        #print(x,y, f1(x,y), f2(x,y))
        x = x1
        y = y1
        
    print(x,y)
    
   
# GAUSS METHOD
def upperTriang(amatrix):
    dimV = len(amatrix)
    for diag in range(dimV):
        aux = amatrix[diag][diag]
        # Dividir todos os membros pelo pivot, para ficar uma diagonal 1
        for col in range(dimV + 1):
            amatrix[diag][col] /= aux
        for lin in range(diag + 1, dimV):
            aux2 = amatrix[lin][diag]
            for col in range(diag, dimV + 1):
                amatrix[lin][col] -= amatrix[diag][col] * aux2

    return amatrix

def lowerTriang(amatrix):
    dimV = len(amatrix)
    for diag in range(dimV - 1, -1, -1):
        for lin in range(diag - 1, -1, -1):
            aux = amatrix[lin][diag]
            for col in range(diag, dimV + 1):
                amatrix[lin][col] -= amatrix[diag][col] * aux

    return amatrix


def printMatrix(amatrix):
    for line in amatrix:
        print("%.05f %.05f %.05f | %.05f" % (line[0], line[1], line[2], line[3]))


if __name__ == "__main__":
    matrix = [[3, 6, 9, 39],
              [2, 5, -2, 3],
              [1, 3,-1, 2]]

    print("Alinea a)")
    printMatrix(upperTriang(matrix))
    print()
    print("Alinea b)")
    printMatrix(lowerTriang(upperTriang(matrix)))

#DA: zeromatrix(4,4) + da;
#DB: zeromatrix(4,1) + db;
#X: col(AB,5);
#DP: DB-DA.X;
#AP: addcol(A,DP);
#AP: echelon(AP);
#AP: rowop(AP,1,2,5); ......
#AP: subst([da=0.3,db=0.3],AP);