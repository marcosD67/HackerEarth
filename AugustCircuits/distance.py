#Result: 100/100
#Solved: 59:39:05
#Constraints were small enough for a brute force approach to work
import numpy as np
 
n = int(input())
 
arr = [int(x) for x in input().split()]
arr = np.array(arr)
for tc in range(int(input())):
  line = input().split()
 
  command = int(line[0])
 
  if command != 3:
    l, r, x = int(line[1]), int(line[2]), int(line[3])
    l -= 1
    r -= 1
    if command == 1:
      arr[l:r+1] += x
    else:
      arr[l:r+1] *= x
  else:
      z = int(line[1])
      res = np.where(arr == z)
      # for i, el in enumerate(res):
      #   print(i, ":")
      #   for index, ele in enumerate(el):
      #     print(index, ele)
      if not res:
        print(-1)
      else:
        print(res[0][-1] - res[0][0] + 1)