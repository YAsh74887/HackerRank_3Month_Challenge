import string

s = "We promptly judged antique ivory buckles for the prize"
s = s.lower().replace(" ","")
s = [*set(s)]
s.sort()

q=list(string.ascii_lowercase)

if len(s) == len(q):
  print("pangram")
else:
  print("not pangram")  
    

