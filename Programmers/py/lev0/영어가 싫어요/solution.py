def solution(numbers):
    alpha=["zero","one","two","three","four","five","six","seven","eight","nine"]
    for idx,val in enumerate(alpha):
        numbers = numbers.replace(val, str(idx))
    return int(numbers)


ans = "onetwothreefouronefivesixseveneightnine"	
print(solution(ans))