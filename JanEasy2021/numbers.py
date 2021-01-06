#Result: 100/100
#Solved: 0:15:29
'''
Answer:
    (Greedy Algorithm)
    Generate all powers of k <= n
    once generated, start from the largest powers first then traverse the list backwards
        ex: k = 3, n = 15, powers = [1, 3, 9, 27] (traverse from 27 -> 1)
    subtract the current power from n iff n >= current power
    at the end, if n is 0, we print yes else we print no 

    Generation of the powers array is O(log(N, K)) base K
    Traversal/Reversal is O(n)
    
'''
from math import log, ceil
 
for tc in range(int(input())):
  n, k = [int(x) for x in input().split()]
  
 
  powers = [1] + [k] + [] #list to hold our powers of k
  p = 2
  while powers[-1] < n:
    powers.append(pow(k, p)) #add new power to the list
    p+=1 #next power
  
  #start traversal from the back of the list
  for i in reversed(powers):
    if n >= i: #if n >= current power...
      n -= i #...subtract it from n
  print("YES" if not n else "NO") #if n is zero, print YES else print NO