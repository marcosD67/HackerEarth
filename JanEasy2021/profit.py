#Results: 100/100
#Solved: 0:03:27
#First in the competition to solve it, but a glitch gave some one else 137/100 points
#so they got the official credit on HackerEarth :(
'''
Answer: 
    convert given list into a set to remove duplicates
    sort list in descending order
    take the largest k elements of the resulting list
    print your answer
'''
for tc in range(int(input())):
  n, k = [int(x) for x in input().split()]
 
  arr = [int(x) for x in input().split()]
  arr = list(set(arr)) #convert given list to a set, then back to a list
  arr.sort(reverse = True) #sort in descending order
 
  ans = 0
 
  #take the largest k elements in the list
  for x in arr:
    if not k: break
    ans += x
    k -= 1
  print(ans)