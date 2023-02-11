
def camelcase(a):
    a = a.split(";")

    try:
        for i in a:
            if i == "S" and len(a[2]) == 4:
                a = a[2].lower()
                a = a[0] + " "+ a[1:]
                print(a) 
            elif i == "C" and len(a[2]) == 9:
                a = a[2].split(" ")
                a = a[0] + a[1].capitalize()  + "()"
                print(a)
            elif i == "S" and len(a[2]) == 17:
                a = a[2].lower()
                a = a[:6] + " " + a[6:]
                print(a)
            elif i == "C" and len(a[2]) == 10:
                a = a[2].split(" ")
                a = a[0].capitalize() + a[1].capitalize()
                print(a)

    
    except:
        pass 
    


a= ["S;V;iPad","C;M;mouse pad","C;C;code swarm","S;C;OrangeHighlighter"]      
for i in a:
    camelcase(i)  