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

def table_printer(matrix):
    
    print("")
    print("     1   2   3   4")
    print("1 ", matrix[0][:])
    print("1 ", matrix[1][:])
    print("1 ", matrix[2][:])
    print("1 ", matrix[3][:])
    print("")



listA = [[x for x in range(1,9)],[x for x in range(1,9)]]

listB = [ j for i in listA for j in i]

random.shuffle(listB)

arrayA = np.array(listB)

matrix = arrayA.reshape(4,4)

default_value_table = []
for x in range(16):
    default_value_table.append("X")

matrixshow = np.array(default_value_table)
matrixshow = matrixshow.reshape(4,4)

falses = [False]*16
matrixflag = np.array(falses)
matrixflag = matrixflag.reshape(4,4)
#table_printer(matrixshow)

score = 0
tries = 10

clear()

while tries > 0:
    print("SCORE: %d" % score)
    print("TRIES: %d" % tries)
    table_printer(matrixshow)
    user_input = input("insert coordinates")

    clear()
    
    xaxis1 = int(user_input[0]) - 1 
    yaxis1 = int(user_input[1]) - 1

    matrixshow[xaxis1][yaxis1] = matrix[xaxis1][yaxis1]
    table_printer(matrixshow)

    time.sleep(3)
    
    if matrixflag[xaxis1][yaxis1] == False:
        chose1 = matrix[xaxis1][yaxis1]
        print("you chose: %d \n" % chose1)
    else:
        print("You chose a card you already revealed! Repeat!\n")
        continue
        
    user_input = input("insert coordinates")
    clear()
    
    xaxis2 = int(user_input[0]) - 1
    yaxis2 = int(user_input[1]) - 1

    chose2 = matrix[xaxis2][yaxis2]
    
    matrixshow[xaxis2][yaxis2] = matrix[xaxis2][yaxis2]
    print("SCORE: %d" % score)
    print("TRIES: %d" % tries)

    table_printer(matrixshow)

    print("you chose: %d \n" % chose2)

    time.sleep(3)
    clear()
    
    if chose1 == chose2:
        print("RIGHT!\n")
        score += 1
        matrixflag[xaxis1][yaxis1] = True
        matrixflag[xaxis2][yaxis2] = True
#        print("Tries you still have: ", tries, "\n")
    else:
        print("WRONG!\n")
        tries -= 1
#        print("Tries you still have: ", tries, "\n")
        matrixshow[xaxis1][yaxis1], matrixshow[xaxis2][yaxis2] = ("X", "X")

if tries == 0:
    print("You loose!")
