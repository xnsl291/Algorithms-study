def solution(phone_number):
    tmp = ["*" for i in range(len(phone_number)-4)]
    return "".join(tmp) + phone_number[-4:]

