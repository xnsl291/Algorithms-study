def result_check(arr):
    result = 0 
    
    scores = [arr[5+i] for i in range(arr[3])]

    if ( (arr[0] * arr[2] *0.01) > arr[1]  ):
        result = [1 if score>arr [4] else 0 for score in scores ]
        return True if (sum(result) == arr[3]) else False
    else:
        return False
			
lec_num = int(input())

info_lst = []
for i in range(lec_num):
    info_lst.append( list(map(int,input().split() )) )
		
flag = [ result_check(info_lst[i]) for i in range(lec_num)]
 
print ( 0 if False in flag else 1)