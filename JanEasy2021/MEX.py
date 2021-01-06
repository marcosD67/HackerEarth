#Result: 10/100 TLE
#Solved: 0:30:00
'''
    Naive solution
    Find all gcds of every subarray of size 2 -> Time Complexity: O(n^2)
    Find first natural number not in resulting set -> Time Complexity: O(100000) (max gcd possible is 100000)

'''
from math import gcd
for tc in range(int(input())):
  n = int(input())
  arr = [int(x) for x in input().split()]
  new = set()
  arr = list(set(arr))
  n = len(arr)
  for i in range(n):
    for j in range(i+1, n):
      new.add(gcd(arr[i], arr[j]))
  # print(new)
 
  test = 1
 
  while True:
    if test not in new:
      print(test)
      break
    test+=1