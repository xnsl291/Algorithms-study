input = input()

try:
    answer = ord(input)
except:
    answer = chr(int(input))

print(answer)