import sys
time = list(map(int,sys.stdin.readline().split()))
require = int(sys.stdin.readline())

hour = time[0]
min = time[1]

if min+require>59:
    hour+=((min+require)//60)
    min = (min+require)%60
    if hour>23:
        hour-=24
else:
    min+=require

print(f"{hour} {min}")
