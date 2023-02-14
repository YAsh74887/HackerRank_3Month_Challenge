
sticks = [1,2,3,4,5,10]

sticks.sort()
i = len(sticks) - 3
while i >= 0 and sticks[i] + sticks[i+1] <= sticks[i+2]:
    i -= 1
if i >= 0:
    print (sticks[i], sticks[i+1], sticks[i+2] )
else:
    print (-1)