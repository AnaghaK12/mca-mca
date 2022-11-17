                                                                                                                                                                                                               s=input("enter the string")
w={}
for wd in s.lower().split():
    w[wd]=w.get(wd,0)+1
print(w)
