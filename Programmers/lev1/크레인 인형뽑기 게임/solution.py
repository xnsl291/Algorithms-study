def solution(board, moves):  
    new_list = [list(i) for i in zip(*board)]
    #[(0, 0, 0, 4, 3), (0, 0, 2, 2, 5), (0, 1, 5, 4, 1), (0, 0, 0, 4, 3), (0, 3, 1, 2, 1)]
    tmp = [] 
    cnt = 0

    for i in moves: 
        for j in range(len(new_list[0])): 
            if new_list[i-1][j] !=0:
                
                if len(tmp) > 0 :
                    if tmp[-1] == new_list[i-1][j]:
                        cnt+=2
                        new_list[i-1][j] = 0
                        tmp.pop(-1)
                        break
                    else: 
                        tmp.append(new_list[i-1][j])
                        new_list[i-1][j] = 0
                        break
                else:
                    tmp.append(new_list[i-1][j])
                    new_list[i-1][j] = 0
                    break
    return cnt
