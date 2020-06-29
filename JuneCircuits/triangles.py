#Result: 45/100 MLE
#Solved: 4:56:13
#Brute force solution attempt
for tc in range(int(input())):
  n, b1, b2 = [int(x) for x in input().split()]
  if n == 5: 
    print(1)
  else:
    count = 0
    vertex = 1
    triangles = set()
    while vertex <= n:
      if vertex != b1 and vertex != b2:
          minusOne = n if vertex-1 < 1 else vertex-1
          plusOne = 1 if vertex+1 > n else vertex+1
          for i in range(1, n+1):
            if i != vertex and i != b1 and i != b2 and i == minusOne:
              for j in range(1, n+1):
                if j != i and j != vertex and j != minusOne and j != b1 and j != b2:
                    curr = (vertex, i, j)
                    curr = sorted(curr)
                    if tuple(curr) not in triangles:
                      triangles.add(tuple(curr))
          for j in range(1, n+1):
             if i != vertex and i != b1 and i != b2 and i == plusOne:
              for j in range(1, n+1):
                if j != i and j != vertex and j != plusOne and j != b1 and j != b2:
                    curr = (vertex, i, j)
                    curr = sorted(curr)
                    if tuple(curr) not in triangles:
                      triangles.add(tuple(curr))  
 
      vertex+=1
    print(len(triangles))