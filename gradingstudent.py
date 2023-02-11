a = [73,67,38,33]



base = 5
for i in range(len(a)):
  if a[i] >= 38:
    k = base * round((a[i]+1)/base)
    if k - a[i] >= 3:
      print(a[i])
    elif k - a[i] < 3:
      print(k)
      
  else:
    print(a[i])    
    
    
       
    
 
  
  
  
  
  
  
  # for i in range(5,100,5):
  #   if a[l]+5 > i:
  #     v.append(i)
  # v = v[-1]   

  # if a[l] < 40:
  #   print(a)    
  # elif v -a[l] >= 3:
  #   print(a)  
  # elif a[l] - v < 3:
  #   print(v)
    


  