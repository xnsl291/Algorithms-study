def solution(board, moves):  
    new_list = [list(i) for i in zip(*board)]
    tmp = [] 
    cnt = 0

    for i in moves: 
        for j in range(len(new_list[0])): 
            if new_list[i-1][j] !=0:
                
                if len(tmp) > 0 and tmp[-1] == new_list[i-1][j]:
                    cnt+=2
                    new_list[i-1][j] = 0
                    tmp.pop(-1)
                    break
                
                else:
                    tmp.append(new_list[i-1][j])
                    new_list[i-1][j] = 0
                    break
    return cnt

b= [[0,0,0,0,0],[0,0,1,0,3],[0,2,5,0,1],[4,2,4,4,2],[3,5,1,3,1]]
m =	[1,5,3,5,1,2,1,4]
print(solution(b,m))