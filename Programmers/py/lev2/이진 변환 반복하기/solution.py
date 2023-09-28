def convert_bin(input,cnt):
    # input 에서 0 제거 & 개수 리턴 
    # input = input.replace('0','')
    input= list(input)
    for idx,i in enumerate(input):
        if i == '0':
            cnt+=1
            input[idx] = ""
    return cnt,bin(len("".join(input)))[2:]

def solution(input):
    time, cnt =0,0
    while(input!='1'):
        cnt,input = convert_bin(input,cnt)
        time+=1
    return [time,cnt]



