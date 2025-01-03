from datetime import datetime, timedelta

def solution(video_len, pos, op_start, op_end, commands):
    format = "%M:%S"
    sec = 10
    video_len = datetime.strptime(video_len,format)
    op_start = datetime.strptime(op_start,format)
    op_end = datetime.strptime(op_end,format)
    pos = datetime.strptime(pos,format)
    
    if op_start <= pos <= op_end:
            pos = op_end

    for c in commands:
        if c == "prev":
            pos =max( datetime.strptime("0:0",format), pos - timedelta(seconds=sec) )
            
        else:
            pos = min(video_len, pos +  timedelta(seconds=sec))

        if op_start<= pos <= op_end:
            pos = op_end

    return datetime.strftime(pos,format)


## TEST		
video_lens = "34:33"	
pos = "13:00"	
op_start = "00:55"	
op_end = "02:55"	
commands =["next", "prev"]	
result = "13:00"

#video_len = "10:55"	
#pos = "00:05"	
#op_start = "00:15"	
#op_end = "06:55"	    
#commands =["prev", "next", "next"]	
#result = "06:55"




ans = solution(video_lens,pos,op_start,op_end,commands)
print(ans == result)

