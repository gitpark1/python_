import random
import copy

board=[[False for x in range(10)]for y in range(10)]

for r in range(10):
    for c in range(10):
        if(random.random()<0.3):
            board[r][c]=True

test=copy.deepcopy(board)

for r in range(10):
    for c in range(10):
        if board[r][c]:
            print("# ",end="")
        else:
            print(". ",end="")
    print()
print('-game board-\n')

"""
def min_search(arr,a,b,max):
    count=0
    if a>0 and b<max:
        for x in arr[a-1][b-1:b+2]:
            if not x:
                count+=1
        for x in arr[a][b-1:b+2]:
            if not x:
                count+=1
        for x in arr[a+1][b-1:b+2]:
            if not x:
                count+=1
        count-=1
"""

for r in range(10):
    for c in range(10):
        if test[r][c]:
            print("# ",end="")
        else:
         

            print(". ",end="")
    print()
print('-test_board-')


