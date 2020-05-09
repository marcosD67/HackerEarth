#Result: 70/100
#Solved: 2:30:03
#Decided to traverse the chess board using tuples to keep track of 
#last position where I added a *
import sys
n = int(input())
board = [['.' for i in range(n)] for i in range(n)]
if n < 2:
    print('*')
    sys.exit()
elif(n > 2):
    if n % 2 == 0:
        oddLast = ((n//2), 1)
        board[(n//2)][1] = '*'
    else:
        oddLast = ((n//2+1), 1)
        board[(n//2+1)][1] = '*'
    done = False
    board[0][0] = '*'
    last = (0, 0)
    count = 2
    for i in range(n):
        for j in range(n):
            if(j % 2 == 0):
                res = tuple(map(lambda x, y: x-y, (i, j), last))
                if res == (1, 2):
                    board[i][j] = '*'
                    count+=1
                    last = (i, j)
            else:
                res = tuple(map(lambda x, y: x-y, (i, j), oddLast))
                if res == (1, 2):
                    board[i][j] = '*'
                    count+=1
                    oddLast = (i, j)
 
            if count == n-1:
                done = True
                break
        if done:break
else:
    board[0][0] = '*'
for x in board:
    for el in x:
        print(el, end = ' ')
    print()