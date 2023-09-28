def solution(s):
    num_list = [ "zero","one","two","three","four","five","six","seven","eight","nine"]

    for i in range(len(num_list)):
        s = s.replace(num_list[i],str(i))

    return int(s)