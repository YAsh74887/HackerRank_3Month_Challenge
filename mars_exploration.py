
s = "SOSOOSOSOSOSOSSOSOSOSOSOSOS"
count = 0
r = len(s)//3
target = "SOS"*r
for i,j in zip(s,target):
  if i != j:
    count += 1
print(count)    