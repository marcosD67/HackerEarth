#Result: 100/100
#Solved: 0:12:18
#Answer: https://oeis.org/A002061 (Central polygonal numbers sequence) 
for tc in range(int(input())):
  n = int(input())
  print(n**2 - n+1)