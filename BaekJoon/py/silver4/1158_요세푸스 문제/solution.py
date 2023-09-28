n, k = map(int, input().split()) 
queue = list(range(n))
result = [] 
idx = 0

while len(queue) >0:
    idx = (idx + (k-1)) % len(queue)
    result.append( str(queue.pop(idx) ))

print("<%s>" %(", ".join(result)))