def solution(food):
    newArr = []
    for i in range(1,len(food)):
        newArr += str(i) * (food[i]//2)
    back_Arr = newArr[::-1]
    newArr+="0"
    return "".join(newArr+back_Arr)
