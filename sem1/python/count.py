s=input("enter the string")
w={}
for a in s.lower():
    w[a]=w.get(a,0)+1
print(w)
