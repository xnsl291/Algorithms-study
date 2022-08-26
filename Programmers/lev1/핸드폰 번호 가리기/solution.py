def solution(phone_number):
    tmp = ["*" for i in range(len(phone_number)-4)]
    return "".join(tmp) + phone_number[-4:]

# 한줄로 풀어보기
def solution2(phone_number):
    return "*"* (len(phone_number)-4)+ phone_number[-4:]
