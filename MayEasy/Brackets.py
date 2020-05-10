#Result: 28/100
#Solved: 2:44:59
#Naive solution. Counts number of open and closed brackets.
s = list(input())
openCount, closeCount = 0, 0
for x in s:
  if x == '(':openCount+=1
  else:closeCount+=1
if openCount != closeCount:print(0)
else:print(min(openCount, closeCount))