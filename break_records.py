l = [12,24,10,12]

min_score = max_score = l[0]
min_count = max_count = 0
for  i in l:
  if i < min_score:
    min_score = i
    min_count += 1
  elif i > max_score:
    max_score = i
    max_count += 1
    
print(min_count, max_count)     
