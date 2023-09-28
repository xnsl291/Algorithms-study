def solution():
    input_arr= []
    while(True):
        input_ = input()
        if input_ == "=":
            break
        input_arr.append(input_)
        
    i=1
    answer = int(input_arr[0])
    while(i<len(input_arr)):
        num = int(input_arr[i+1])
        if input_arr[i] == "+":
            answer+=num
        elif input_arr[i] == "-":
            answer -=num
        elif input_arr[i] == "/":
            answer //= num
        elif input_arr[i] == "*":
            answer*= num
        i+=2
    return answer
    
        

print(solution())