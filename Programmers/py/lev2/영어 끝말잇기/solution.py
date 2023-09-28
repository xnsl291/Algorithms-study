def solution(n, words):
    # 1단어 제거 
    for word in words:
        if len(word)<2:
            words.remove(word)
    
    for i, word in enumerate(words):
        # i>0
        if i>0 and ((word in words[:i]) or (words[i-1][-1] != words[i][0])):
            return [i % n + 1, (i//n)+1]
    return [0, 0]

