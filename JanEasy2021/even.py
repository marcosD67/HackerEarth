#Result: 100/100
#Solved: 1:38:51
#had a shorter solution after the contest, but this got me 100 during
'''
    Problem Statement: https://www.hackerearth.com/practice/basic-programming/bit-manipulation/basics-of-bit-manipulation/practice-problems/algorithm/make-even-8ced0d4b/
    Just do as the problem is asking for
    Time Complexity: O(n)

'''

for tc in range(int(input())):
  n = int(input())
  arr = [int(x) for x in input().split()]
  ans = float('inf')
  cop = arr.copy()
  moves, moves2 = 0, 0
  ptr = 0
  while ptr < n:
    if arr[ptr] % 2 != 0: 
      if ptr == n-1:
        ptr-=1
      while arr[ptr] % 2 != 0 or arr[ptr+1] % 2 != 0:
        hold, temp = arr[ptr], arr[ptr+1]
        arr[ptr] = hold + temp
        arr[ptr+1] = hold - temp
        moves +=1
    ptr+=1
  # print(arr)
  ptr = n-1
 
  while ptr >= 0:
    if cop[ptr] % 2 != 0:
      if ptr == n-1:
        ptr-=1
      while cop[ptr] % 2 != 0 or cop[ptr+1] % 2 != 0:
        hold, temp = cop[ptr], cop[ptr+1]
        cop[ptr] = hold + temp
        cop[ptr+1] = hold - temp
        moves2 +=1
    ptr-=1
  # print(cop)
  print(min(moves, moves2))