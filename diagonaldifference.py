
primary = 0
secondary = 0
arr = [[11, 2, 4], [4, 5, 6], [10, 8, -12]]
for i in range(len(arr)):
  primary = primary + arr[i][i]  

count = len(arr[1])-1
for i in range(len(arr)):
  secondary = secondary + arr[i][count]
  count = count -1

print(abs(primary-secondary))