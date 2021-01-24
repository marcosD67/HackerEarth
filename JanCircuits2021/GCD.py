#Result: 100/100
#Solved: 3:39:53
#The first answer was simply the sum of natural numbers from 1 - n
#the second answer was the LCM from 1-n (I used the prime divisors method to find this)
from math import gcd
MAX = 41
primes = [True for i in range(MAX)]
primeNums = []
primes[0] = primes[1] = False
p = 2
 
while p * p <= MAX:
  if primes[p]:
    for i in range(p*p, MAX+1, p):
      primes[i] = False
  p += 1
 
for i, x in enumerate(primes):
  if x: primeNums.append(i)
 
def LCM(n):
  lcm = 1
  i = 0
 
  while i < len(primeNums) and primeNums[i] <= n:
    curr = primeNums[i]
 
    while curr * primeNums[i] <= n:
      curr *= primeNums[i]
    lcm *= curr
    i += 1
  return lcm
for tc in range(int(input())):
  n = int(input())
 
  total = n * (n+1) // 2
  x = LCM(n)
  print(total, x)