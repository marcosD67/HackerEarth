#Result: 100/100
#Solved: 112:07:12
#When to print -1
    #When m > n + (n+1) // 2
    #when m < n + (n-1)
#else:
    #Greedy Solution
    #Observation: (If using 1-based leveling) then each added node contributes it's level to the current sum
    #make a base tree with 1->2
    #Repeat below until all n nodes have been placed
        #then greedily consider the number of nodes we have left to place
        #if the numder of nodes left to place * level (that I'm currently on) < m
            # then move to the next level
        #else if the numder of nodes left to place * level (that I'm currently on) > m
            # go to previous level
        #else
            # stay on current level until m is reached
    
n, m = [int(x) for x in input().split()]
 
limit = n * (n+1) // 2
 
if m < n + (n-1):
  print(-1)
elif m > limit:
  print(-1)
else:
  #READ: I used 0-based leveling, hence i did m -= (level+1) rather than just m -= level
  tree = [[] for i in range(n+1)] #2d list to represent tree
  tree[0].append(1)
  tree[1].append(2)
 
  m -= 3
  nodesLeft = n-2
  curr = 3
 
  currLevel = 1
  while nodesLeft:
    if nodesLeft * (currLevel + 1) > m: #this would cause us to go over m
      currLevel -= 1 #move to previous level
    else:
      if nodesLeft * (currLevel+1) < m: #this would cause us to go below m
        currLevel += 1 #move to next level
      if currLevel > n+1: #handle possible out of bounds error
        currLevel -= 1
    
    tree[currLevel].append(curr)
    curr += 1
    nodesLeft -= 1
    m -= currLevel+1
 
    #print final tree
  for i in range(n+1):
    if not i:
      if len(tree[i]) > 1:
        for x in tree[i][1:]:
          print(1, x)
    else:
      for x in tree[i]:
        print(i, x)