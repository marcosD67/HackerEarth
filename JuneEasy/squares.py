#Result: 100/100 
#Solved: 0:25:42
#O(1) Time Complexity
for tc in range(int(input())):
  l, r = [int(x) for x in input().split()]
  count = (r//4) - ((l-1)//4) #counts multiples of 4 in the range
  odds = (r-l)//2 #counts number of odds in the range
  if r % 2 != 0 or l % 2 != 0: #count the limit range if either is odd
    odds+=1
  print(count+odds) #solution is the addition of both results