picture = [
    [0,0,0,1,0,0,0],
    [0,0,1,1,1,0,0],
    [0,1,1,1,1,1,0],
    [1,1,1,1,1,1,1],
    [0,0,0,1,0,0,0],
    [0,0,0,1,0,0,0]
]
def tree_cri():
    for line in picture:
        for number in line:
            if (number == 1) :
                print('*' , end='')
            else:
                print(' ' , end='')
        print('')

print(tree_cri())