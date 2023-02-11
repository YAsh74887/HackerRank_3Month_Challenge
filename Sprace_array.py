from collections import Counter
string = ['aba', 'baba', 'aba', 'xzxb']
query = ['aba', 'xzxb', 'ab']

result = []
s = Counter(string)


for q in query:
  result.append(s[q])
  
print(result)  

