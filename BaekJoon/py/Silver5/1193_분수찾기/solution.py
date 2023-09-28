num = int(input())

lst= [1]
for i in range(1,num):
    next = lst[-1]+i
    if num >= next:
        lst.append(next)
    else:
        break

sub = num-lst[-1]
print(f"{1+sub}/{len(lst)-sub}") if len(lst)%2 ==0 else print(f"{len(lst)-sub}/{1+sub}")

    




