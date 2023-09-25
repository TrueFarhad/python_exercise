import time
import os
# main arrow
matrix = [
    [0,0,0,1,0,0,0],
    [0,0,1,1,1,0,0],
    [0,1,1,1,1,1,0],
    [1,1,1,1,1,1,1],
    [0,0,0,1,0,0,0],
    [0,0,0,1,0,0,0]
]
# showing arrow as default
def matrix_top(matrix):
   for row in matrix:
    for pix in row:
        if pix==0:
         print(" ", end=' ')
        elif pix ==1:
            print("*",end=' ')
    print("\r")

# showing arrow as reverse default
def matrix_bottem(matrix):
   for row in matrix[::-1]:
    for pix in row:
        if pix==0:
         print(" ", end=' ')
        elif pix ==1:
           print("*",end=' ')
    print("\r")



# making function to rotate arrow to the right

def rotate_matrix_right(matrix):
    transposedx = []
    for row in zip(*matrix):
        transposedx.append(list(row))
    rotatedx = []
    for row in transposedx:
        rotatedx.append(row[::-1])
    return rotatedx


rotate_90 = rotate_matrix_right(matrix)
# it shows the rotate arrow 
def matrix_right(rotate_90):
    for row in rotate_90:
        for pix in row:
            if pix==1:
                print("*",end='')
            elif pix==0:
                print("",end=' ')    
        print("\r")

# again making new rotation to the left
def rotate_matrix_left(matrix):
    transposed = []
    for row in zip(*matrix):
        transposed.append(list(row))
    rotated = []
    for row in transposed:
        rotated.append(row[::1])
    return rotated


rotate_270 = rotate_matrix_left(matrix)
# it shows the rotated arrow
def matrix_left(rotate_270):
    for row in rotate_270:
        for pix in row:
            if pix==1:
                print("*",end='')
            elif pix==0:
                print("",end=' ')    
        print("\r")

# arrow_rotation =[matrix_top(matrix),matrix_right(rotate_90),matrix_bottem(matrix),matrix_left(rotate_270)]
count=0
countdown_Loop = 4
# showing arrow rotation clockwise
countdown = 0
while count< countdown_Loop * 4:
    time.sleep(2)
    os.system('cls' if os.name == 'nt' else 'clear') # clear the terminal
    
    if(countdown == 0):
       matrix_top(matrix)
    elif(countdown == 1):
       matrix_right(rotate_90)
    elif(countdown == 2):
       matrix_bottem(matrix)
    elif(countdown == 3):
       matrix_left(rotate_270)
    
    countdown = countdown + 1
    if(countdown == 4):
        countdown = 0

    count = count + 1