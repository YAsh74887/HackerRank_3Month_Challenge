A = [1, 2, 2, 1]
B = [3, 3, 3, 4]
k = 5


A.sort()
B.sort()
B.reverse()

count = 0
for i in range(len(A)):
  if A[i] + B[i] >= k:
    count = count  + 1

if count == len(A):
  print("YES")
else:
  print("NO")  
  
      