#Result: 100/100
#Solved: 0:30:51
for tc in range(int(input())):
  n = int(input())
  arr = [int(x) for x in input().split()]
  arr = set(arr)
  print(sum(arr))