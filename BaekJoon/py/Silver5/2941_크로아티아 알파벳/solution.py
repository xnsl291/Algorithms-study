import re
new = list(input())
new_alpha= ["c=", "c-" "d-", "lj", "nj", "s=", "z="]

for i in range(len(new)-1):
    if new[i]+new[i+1] in new_alpha:
        new[i+1] = ''
    if new[i]+new[i+1]=='dz':
        try:
            if new[i+2]=="=":
                new[i+1] = ""
                new[i+2]=""
        except:
            continue

print(len(list(re.sub('[-=]',"","".join(new)))))
