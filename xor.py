
s = "10101"
t = "00101"

res = []
for i in range(len(s)):
    if s[i] == t[i]:
        res.append(0)
    else:
        res.append(1)
        
for x in res:
  print(x,end="")        
      