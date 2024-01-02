def solution(progresses, speeds):
    answer = [] 
    prev, period, count = 0, 0, 0

    for i in range(len(progresses)):
        period = ((100 - progresses[i]) / speeds[i] )
        period += 1 if period*10%10 >0 else 0
        
        if i == 0 : 
            prev = period
            pass

        if period > prev:
            answer.append(count)
            count = 1 
            prev = period 

        else:
            count += 1 
            
    answer.append(count)
    return answer

progresses = [93, 30, 55]
speeds = [1, 30, 5]

# progresses = [95, 90, 99, 99, 80, 99]
# speeds = [1, 1, 1, 1, 1, 1]
print(solution(progresses, speeds))

