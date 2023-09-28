info = list(map(int,input().split() ))
vocabs = [ input() for i in range(info[0])]

vocabs.sort()
vocabs.sort(key=len)
print(vocabs[info[1]-1])