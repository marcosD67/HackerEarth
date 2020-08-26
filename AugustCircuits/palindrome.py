#Result: 100/100
#Solved: 39:48:03
#Sort string and check if string is all the same character ex: aaaaa...
for tc in range(int(input())):
  s = list(input())
  s.sort()
 
  if s.count(s[0]) == len(s): #couldve been replaced by: if(s[0] == s[-1]) and been more efficient
    print(-1)
  else:
    print(*s, sep = '')