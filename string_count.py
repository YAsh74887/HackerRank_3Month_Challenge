
a = "engineering"
q=[*set(a)]
q.sort()

for i in range(len(q)):
  f = a.count(q[i])
  print(f"{q[i]} = {f}")