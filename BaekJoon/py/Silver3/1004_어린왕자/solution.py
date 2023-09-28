import sys

def isIn(points , x,y,r):
    cnt = 0  
    # 점 간 거리 vs 반지름길이 비교
    start_dist = (points[0]-x)**2+(points[1]-y)**2
    end_dist = (points[2]-x)**2+(points[3]-y)**2

    if start_dist < r**2 and end_dist < r**2:
        # 같은 원안에 들어있을 경우 제외 
        pass
    elif start_dist < r**2 :
        cnt+=1
    elif end_dist < r**2:
        cnt+=1
    return cnt


test_num = int(sys.stdin.readline())

for test in range(test_num):
    cnt = 0 
    points = list(map(int, sys.stdin.readline().split()))
    planet_cnt = int(sys.stdin.readline())

    for i in range(planet_cnt):
        x,y,r = map(int, sys.stdin.readline().split())
        cnt+=isIn(points, x,y,r)

    print(cnt)