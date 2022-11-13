#solution 1
def solution1(arr1,arr2):
    for i in range(len(arr1)):
        for j in range(len(arr1[0])):
            arr1[i][j] += arr2[i][j]
    return arr1
                 
#solution 2 - 1줄로 작성하기/ zip함수 중첩사용
def solution2(arr1,arr2):
  return [[i+v for i,v in zip(a1,a2)] for a1,a2 in zip(arr1,arr2)]
