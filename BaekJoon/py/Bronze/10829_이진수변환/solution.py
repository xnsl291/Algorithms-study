#while문 
n = int(input())

lst = []
while n>0:
    lst.insert(0,str(n%2))
    n = n//2 if n//2 != 1 else 1

print("".join(lst))  



