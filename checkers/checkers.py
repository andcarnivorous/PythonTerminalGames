import time
import os
import numpy as np
import random

def clear(): 

    name = os.name
    if name == 'nt': 
        os.system('cls') 
  
    else: 
        os.system('clear') 
        
def table_printer(matrix, score):
    
    print("")
    print("     1 2 3 4 5 6 7 8   ")
    print("  ____________________")
    print("1 |", matrix[0][:])
    print("2 |", matrix[1][:])
    print("3 |", matrix[2][:])
    print("4 |", matrix[3][:])
    print("5 |", matrix[4][:])
    print("6 |", matrix[5][:])
    print("7 |", matrix[6][:])
    print("8 |", matrix[7][:])
    print("")

    return "SCORE: %d" % score

arrayA = np.array([range(1,65)])

matrix = np.zeros(shape =(64), dtype = int)

seriesA = [x for x in range(0,16,2)]

for x in range(40,48):
    if x % 2 == True:
        matrix[x] = 1

for x in range(48,56):
    if x % 2 == False:
        matrix[x] = 1

for x in range(56,64):
    if x %2 == True:
        matrix[x] = 1
        
for x in range(0,8):
    if x % 2 == False:
        matrix[x] = 2

for x in range(8,16):
    if x % 2 == True:
        matrix[x] = 2

for x in range(16,24):
    if x %2 == False:
        matrix[x] = 2


matrix = matrix.reshape(8,8)

score = 0

for x in range(6):
    print("\n", table_printer(matrix, score))


    choose = input("insert coordinates: ")
    a = int(choose[0]) -1
    b = int(choose[1]) -1
    print(matrix[a][b])

    if matrix[a][b] == 1:

        choose = input("insert coordinates: ")
        c = int(choose[0]) -1
        d = int(choose[1]) -1

        if matrix[c][d] == 0:
#            print(matrix[c][d])
            if c == a+1 or c == a-1:
                if d == b+1 or d == b-1:
                    matrix[a][b] = 0
                    matrix[c][d] = 1

        elif matrix[c][d] == 2 and -1 not in [c-1,d-1] and 9 not in [c+1,d+1]:
            if c == a+1:
                if d == b+1:
                    matrix[a][b] = 0
                    matrix[c][d] = 0
                    matrix[c+1][d+1] = 1
                    score += 1
                    
                elif d == b-1:
                    matrix[a][b] = 0
                    matrix[c][d] = 0
                    matrix[c+1][d-1] = 1
                    score += 1
                    
            elif c == a-1:
                if d == b+1:
                    matrix[a][b] = 0
                    matrix[c][d] = 0
                    matrix[c-1][d+1] = 1
                    score += 1
                    
                elif d == b-1:
                    matrix[a][b] = 0
                    matrix[c][d] = 0
                    matrix[c-1][d-1] = 1
                    score += 1
                    
        else:
            print("wrong input!")

        
