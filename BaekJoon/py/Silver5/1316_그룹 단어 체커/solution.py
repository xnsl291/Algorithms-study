def check_word(word):
    flag = 0
    used_alpha = []

    for alpha in word:
        if alpha not in used_alpha:
            used_alpha.append(alpha)
            head = alpha
        elif alpha != head:
            return 0
    return 1

num = int(input())
answer = 0
for i in range(num):    
    word = input()
    num = check_word(word)
    answer+= num
    
print(answer)
    