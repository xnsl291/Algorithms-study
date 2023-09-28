def solution(sizes):
    row,column = [list(i) for i in zip(*sizes)]

    for i in range(len(sizes)):
        if row[i]> column[i]:
            row[i],column[i] = column[i],row[i] 
    return max(row)*max(column)
