steps = 8 
path = "UDDDUDUU"
valleycount = level = 0
d={'U': 1, 'D': -1}
for i in path:
  level += d[i]
  if level == 0 and i == "U":
    valleycount += 1	        
print ( valleycount)
