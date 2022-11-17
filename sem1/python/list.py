n=input("enter a list of number:")
n=list(map(int,n.split()))
p=[num for num in n if num%2]
print(p)
