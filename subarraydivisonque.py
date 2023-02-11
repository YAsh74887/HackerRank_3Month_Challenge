
s = [2,2,1,3,2]
d = 4
m = 2

count = 0

for i in range(len(s)):
  if sum(s[i:m+i]) == d:
    count = count + 1
    
print(count)    