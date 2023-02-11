
ar = [1, 3, 2, 6, 1, 2]
ar.sort
n=len(ar)
k=3
o = 0
count = 0
for i in range(n):
  for j in range(i+1, n): 
    if (ar[i] + ar[j]) % k == 0:
      count = count + 1
print(count)         
                
      



