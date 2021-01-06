#Result: 24/100
#Solved: 26:54:16
for tc in range(int(input())):
  n, m, k = [int(x) for x in input().split()]
 
  if n == 1 or m == 1:
    print("No")
    continue
  total = n*m
  if k > total:
    print("No")
  elif total % 2 == 0 and k % 2 == 0:
    print("Yes")
  elif total % 2 != 0 and k % 2 != 0:
    print("Yes")
  else:
    print("No")