picture = [
    [0,0,0,1,0,0,0],
    [0,0,1,1,1,0,0],
    [0,1,1,1,1,1,0],
    [1,1,1,1,1,1,1],
    [0,0,0,1,0,0,0],
    [0,0,0,1,0,0,0]
]
for row in picture[::1]:
    for pix in row:
        if pix==0:
         print(" ", end=' ')
        elif pix ==1:
           print("*",end=' ')
    print("\r")