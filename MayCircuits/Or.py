#Result: 40/100
#Solved: 123:42:23
# from math import log
a = int(input())
b = int(input())
if a == b:print(1)
else:
  seen = set()
  count = (b-a)+1
  for i in range(a, b+1):
    for j in range(i, b+1):
      res = i
      # print(i, "|=", j)
      # print(bin(i)[2:].zfill(8), '|', bin(j)[2:].zfill(8), end = ' = ')
      res |= j
      # print(res)
      if 0 < res > b:
        seen.add(res)
  
    # print()
  # print(seen)
  print(len(seen)+count)