n = input()
f = int(input())

tmp = int(n[:-2]+'00')

while True:
    if tmp %f == 0:
        break
    tmp +=1
    
print(str(tmp)[-2:])