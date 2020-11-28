#Result: 100/100
#Simulate playing the game
n = int(input())
 
black = [int(x) for x in input().split()]
white = [int(x) for x in input().split()]
 
red = int(input())
 
a,b,c,d = [int(x) for x in input().split()]
 
wVisited, bVisited = [0 for i in range(n)], [0 for i in range(n)]
turn = 1
done = False
while not done:
  if turn % 2 == 1:
    index = -1
    pawnsLeft = False
    if turn == 1:
      for i, x in enumerate(black):
        if not bVisited[i]:
          pawnsLeft = True
          if a >= x:
            index = i
            break
      if not pawnsLeft:
        if a >= red:
          done = True
          print("A-C")
        else: a += 1
      if index == -1:
        a += 1
      else: bVisited[index] = 1
    else: #turn == 3
      for i, x in enumerate(black):
        if not bVisited[i]:
          pawnsLeft = True
          if c >= x:
            index = i
            break
      if not pawnsLeft:
        if c >= red:
          done = True
          print("A-C")
        else: c+=1
      if index == -1:
        c += 1
      else: bVisited[index] = 1
  else:
      index = -1
      pawnsLeft = False
 
      if turn == 2:
        for i, x in enumerate(white):
          if not wVisited[i]:
            pawnsLeft = True
            if b >= x:
              index = i
              break
        if not pawnsLeft:
          if b >= red:
            done = True
            print("B-D")
          else: b+=1
        if index == -1:
          b += 1
        else: wVisited[index] = 1
      else:
        for i, x in enumerate(white):
          if not wVisited[i]:
            pawnsLeft = True
            if d >= x:
              index = i
              break
        if not pawnsLeft:
          if d >= red:
            print("B-D")
            done = True
          else: d+=1
        if index == -1:
          d += 1
        else: wVisited[index] = 1
  turn %= 4
  turn+=1