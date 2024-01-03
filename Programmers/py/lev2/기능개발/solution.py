def newsolution(progresses,speeds):
    answer = []
    period, count = 0,0
    while(len(progresses)>0):
        if (progresses[0] + period*speeds[0]) >= 100: 
            progresses.pop(0)
            speeds.pop(0)
            count += 1
            
        else:
            if count > 0:
                answer.append(count)
                count = 0
            period += 1
    answer.append(count)
    return answer

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
print(newsolution(progresses, speeds))
print(solution(progresses, speeds))

