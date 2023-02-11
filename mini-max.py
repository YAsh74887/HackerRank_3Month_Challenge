arr = [1, 2, 3, 4, 5]


min_n = min(arr)
max = max(arr)


min = sum(arr) - max
max = sum(arr) - min_n
print(max)
print(min)