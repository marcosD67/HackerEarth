#Result: 4/100
#Solved: 0:51:47
#Naive solution
from collections import defaultdict
n, m = [int(x) for x in input().split()]
arr = [int(x) for x in input().split()]
happy = [int(x) for x in input().split()]
for tc in range(int(input())):
    isHappy = True
    d = defaultdict(int)
    l, r = [int(x) for x in input().split()]
    for i in range(l-1, r):
      d[arr[i]]+=1
    for k, v in d.items():
      if v != happy[k-1]:
        isHappy = False
        break
    print(1 if isHappy else 0)