#Result: 100/100
#Solved: 0:09:31
#answer was simply sum of n natural numbers plus one!
for tc in range(int(input())):
  n = int(input())
  print(((n * (n+1))//2) + 1)