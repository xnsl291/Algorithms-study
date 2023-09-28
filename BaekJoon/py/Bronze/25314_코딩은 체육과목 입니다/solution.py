import sys
target = int(sys.stdin.readline())
time = target//4 if target%4==0 else target//4+1
print('long '*time+'int')
