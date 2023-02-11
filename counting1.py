arr = [1,1,3,2,1]

count = [0] * 100


for i in arr:
  count[i] += 1

print(count)  