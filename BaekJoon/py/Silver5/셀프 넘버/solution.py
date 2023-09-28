def solution():
    # lst = list(range(1,100))
    lst = list(range(1,10001))

    for i in range(len(lst)):
        next_num = sum([ int(str(i)[j-1]) for j in range(len(str(i)))])+i
        if next_num in lst:
            lst.remove(next_num)

    for i in lst:
        print(i)

solution()