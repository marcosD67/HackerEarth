#Result: 100/100
#Solved: 60:18:57
#Binary Decomposition
for tc in range(int(input())):
  n = int(input())
  
  binary_form = [0] * 64
  i = 0
  while n:
    binary_form[i] = n % 2
    n //= 2
    i += 1
  print(binary_form.count(1))
  for j in range(i):
    if binary_form[j] == 1:
      print(3**j, end = ' ')
  print()