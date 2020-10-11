#Result: 100/100
#Solved: 0:23:15
from math import gcd
for tc in range(int(input())):
  x, y = [int(x) for x in input().split()]

  ans = gcd(x, y)

  if ans and (not (ans & (ans-1))):
    print("Yes")
  else:
    print("No")
