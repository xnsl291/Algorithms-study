input = input().split(" ")
print( max([int("".join(list(reversed(input[0])))),int("".join(list(reversed(input[1]))))]))