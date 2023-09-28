import sys
from queue import PriorityQueue
def solution():
    input = sys.stdin.readline
    num = int(input())
    p_queue = PriorityQueue()
    answer = 0
    for i in range(num):
        p_queue.put(int(input()))
    
    while(p_queue.qsize() > 1):
        sum_val = p_queue.get() + p_queue.get()
        answer += sum_val
        p_queue.put(sum_val)
    return answer
    
print(solution())
