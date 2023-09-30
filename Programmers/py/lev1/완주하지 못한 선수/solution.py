from collections import Counter
def solution(participant, completion):
    complete_map = Counter(completion)
    
    for name in participant:
        if complete_map[name] == 0 :
            return name 
        complete_map[name] -= 1

# 다른 풀이 (정렬활용)
# idea: 
# 두 리스트를 정렬 한 뒤, 인덱스별로 비교하다가 값이 다르면 이름 반환 
# 완주자를 기준으로 비교하므로, 만약 마지막 참여자가 완주하지 못한 사람이라면, 비교하지 못하므로 잠여자[-1] 반환.
def solution(participant, completion):
    participant.sort()
    completion.sort()

    for idx in range(len(completion)):
        if participant[idx] != completion[idx] : 
            return participant[idx]
    return participant[-1]
        
