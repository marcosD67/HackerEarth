#Result: 100/100
#Solved: 2:09:59
from math import gcd
for tc in range(int(input())):
  x, y = [int(x) for x in input().split()]
  if x < y: print(-1)
  else:
    if x < 0 or y < 0: print(-1)
    else: print(max(x, y))