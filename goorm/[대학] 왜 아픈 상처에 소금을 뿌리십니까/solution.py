
# 만약 7을 입력받았다고 하면 7개의 배열중에서 
# 1의 위치의 최대 최소값을 구해서 최소 * 최대 하는데 
# 가로 ( 최대 - 최소 +1 ) * 세로 (최대 - 최소 +1 )

# -*- coding: utf-8 -*-
# UTF-8 encoding when using korean

tmp = []
numbers=[]
min_h, min_w, max_h, max_w = 100, 100, 0 , 0
num = int(input())

for i in range(num):
    # 입력받고 int 변환 
    tmp.append(input().split())
    numbers.append([int (tmp[i][j]) for j in range(len(tmp[0]))] )

    if ( sum(numbers[i]) >0 ): 
        for j in range(num): 
            if (numbers[i][j] == 1 ):
                min_h = i if i < min_h else min_h
                max_h = i if i > max_h else max_h
                min_w = j if j < min_w else min_w
                max_w = j if j > max_w else max_w
        
        result =  (max_h- min_h+1) *   (max_w +1- min_w)  
        
    else:
        result = 0

print(result)

