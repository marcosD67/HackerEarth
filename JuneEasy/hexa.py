#Result: 100/100 
#Solved: 2:46:14
#Solution was to just do what the problem said to do!
from math import gcd
chars = {'a' : 10, 'b' : 11, 'c' : 12, 'd' : 13, 'e' : 14, 'f' : 15}
 
for tc in range(int(input())):
  l, r = [int(x) for x in input().split()]
  count = 0
  for i in range(l, r+1):
    res = str(hex(i)[2:])
    iSum = 0
    for ch in res:
      if ch in chars: iSum += chars[ch]
      else: iSum += int(ch)
    if gcd(i, iSum) > 1:count+=1
  print(count)