a=int(input("enter a value"))
if a<10:
    n1=int("%s"%(a))
    n2=int("%s%s"%(a,a))
    n3=int("%s%s%s"%(a,a,a))
    re=n1+n2+n3
    print("sum",n1,'+',n2,'+',n3, 'is',re)       
       
