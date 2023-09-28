test_num = int(input())

for i in range(test_num):
    ans =""
    target = input().split(" ")
    rep_num = int(target[0])
    rep_str = target[1]
    for j in range(len(rep_str)):
        ans+=rep_str[j]*rep_num
    print(ans)