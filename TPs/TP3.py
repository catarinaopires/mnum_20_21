import math

def f(x):
    return 3*x**3-x-10

def f_linha(x):
    return 9*x**2-1

def metodo_newton(guess, precision):
    x = guess
    
    while True:
        x1 = x - f(x)/f_linha(x)
        t = abs(x1 - x)
        
        if t < precision:
            break
        x = x1
    return x
    

def metodo_picard1(guess, precision):
    x = guess
    
    while True:
        x1 = 3*x^3-10
        t = abs(x1 - x)
        
        if t < precision:
            break
        x = x1
    return x

def metodo_picard2(guess, precision):
    x = guess
    
    while True:
        x1 = (x-10)/x**2
        t = abs(x1 - x)
        
        if t < precision:
            break
        x = x1
    return x


def metodo_picard3(guess, precision):
    x = guess
    
    while True:
        x1 = math.sqrt((x+10)/3*x)
        t = abs(x1 - x)
        
        if t < precision:
            break
        x = x1
    return x