from collections import Counter
numbers = Counter(list(map(int,input().split())))

def solv(numbers):
    if len(numbers.keys())==1:
        return 10000+list(numbers.keys())[0]*1000
    elif len(numbers.keys())==2:
        return 1000+(numbers.most_common()[0][0])*100
    else:
        return (max(numbers.items())[0])*100

print(solv(numbers))
