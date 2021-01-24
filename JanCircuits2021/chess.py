#Result: 100/100
#Solved: 4:27:14

#I used Euclidean distance
#If distance between the two is 1, then first king wins]
#If coordinates are matching, then second king wins
#else DRAW
from math import sqrt
for tc in range(int(input())):
  x1, y1 = [int(x) for x in input().split()]
  x2, y2 = [int(x) for x in input().split()]
 
  if x1 == x2 and y1 == y2:
    print("SECOND")
    continue
  dist = int(sqrt(pow(x2-x1, 2) + pow(y2-y1, 2)))
  if dist > 1:
    print("DRAW")
  else:
    print("FIRST")