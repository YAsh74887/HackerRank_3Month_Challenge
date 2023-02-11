
from collections import Counter
ar = [10, 20, 20, 10, 10, 30, 50, 10, 20]

a = Counter(ar)
v = []
for k in a.values():
  if k//2 >= 1:
    v.append(k//2)
    
print(sum(v))    

