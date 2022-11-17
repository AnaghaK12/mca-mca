strl=input("enter the string")
n=""
for x in strl:
    if(x.isalpha() or x==' '):
        n+=x
print(len(n.split()))
