#Result: 100/100
#Solved: 0:53:08
for tc in range(int(input())):
  n, m = [int(x) for x in input().split()]
  matrix = []
  smallest, greatest = [], []
  for i in range(n):
    row = [int(x) for x in input().split()]
    sm, ma = min(row), max(row)
    for index, x in enumerate(row):
      if x == sm:
        smallest.append((i, index, x))
      elif x == ma:
        greatest.append((i, index, x))
    matrix.append(row)
  
  smallRow, smallCol, smallTarget = [], [], smallest[0][2]
  smallRow.append(smallest[0][0])
  smallCol.append(smallest[0][1])
  for (i, j, x) in smallest[1:]:
    if x < smallTarget:
      smallRow.clear()
      smallCol.clear()
      smallRow.append(i)
      smallCol.append(j)
      smallTarget = x
    elif x == smallTarget:
      smallRow.append(i)
      smallCol.append(j)
  
  largeRow, largeCol, largeTarget = [], [], greatest[0][2]
  largeRow.append(greatest[0][0])
  largeCol.append(greatest[0][1])
  # print("smallest:", smallest)
  # print("greatest:", greatest)
  for (i, j, x) in greatest[1:]:
    if x > largeTarget:
      largeRow.clear()
      largeCol.clear()
      largeRow.append(i)
      largeCol.append(j)
      largeTarget = x
    elif x == largeTarget:
      largeRow.append(i)
      largeCol.append(j)
  # print(smallRow, smallCol)
  # print(largeRow, largeCol)
  count = 0
 
  for i in range(n):
    if i in smallRow or i in largeRow: continue
    for j in range(m):
      if j in smallCol or j in largeCol: continue
      # else:
      #   print(i, j)
      count+=1
  print(count)