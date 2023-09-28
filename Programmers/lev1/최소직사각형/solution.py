def solution(sizes):
    row,column = [list(i) for i in zip(*sizes)]

    for i in range(len(sizes)):
        if row[i]> column[i]:
            row[i],column[i] = column[i],row[i] 
    return max(row)*max(column)

# 리스트 저장대신 값만 반환하는 함수
# result = 최대값 x 최소값들 중 최대값 
def solution2(sizes):
    return max([max(i) for i in sizes])*max([min(i) for i in sizes])
