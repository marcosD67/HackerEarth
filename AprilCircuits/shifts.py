#Result: 100/100
#Solved: 0:40:10
from collections import deque
get_bin = lambda x, n: format(x, 'b').zfill(n)
for tc in range(int(input())):
    line = input().split()
    num, numOfShifts, direction = int(line[0]), int(line[1]), line[2]
    s = deque(get_bin(num, 16))
    if direction == 'L':
        s.rotate(-numOfShifts)
    else:s.rotate(numOfShifts) #to the right
    res = ''.join(s)
    print(int(res, 2))