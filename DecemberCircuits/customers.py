#Result: 38/100
#Solved: 107:16:16
from math import ceil
for tc in range(int(input())):
  n = int(input())
  arr = []
 
  total = 0
  for i in range(n):
    u, v, w = [int(x) for x in input().split()]
    arr.append((u, v, w))
    total += w
  rate = ceil(total / n)
  arr.sort(key = lambda x : x[1])
  totalBooks = 0
  prevEndTime = 0
  for i, (l, r, books) in enumerate(arr):
    if not i:
      totalBooks = l * rate
      prevEndTime = l
    else:
      totalBooks += rate * (l-prevEndTime)
 
    if totalBooks >= books:
      totalBooks -= books
      prevEndTime = l
      continue
    
 
    totalBooks += rate * (r-l)
 
    if totalBooks >= books:
      totalBooks -= books
      prevEndTime = r
    else:
      totalBooks -= rate * (r-l)
      rate += 1
      totalBooks += rate * (r-l)
 
      if totalBooks >= books:
        totalBooks -= books
        prevEndTime = r
      
  print(rate)