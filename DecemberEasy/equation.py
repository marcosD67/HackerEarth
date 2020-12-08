#Result 100/1000
#answer: https://oeis.org/A000217 (Triagular numbers)
b = int(input())
l= b-1
a = l*(l+1)//2
c = b*(b+1)//2
print(a, c)