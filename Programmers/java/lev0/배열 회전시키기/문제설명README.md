# 배열 회전시키기

***

## 문제 설명
정수가 담긴 배열 numbers와 문자열 direction가 매개변수로 주어집니다. 배열 numbers의 원소를 direction방향으로 한 칸씩 회전시킨 배열을 return하도록 solution 함수를 완성해주세요.

## 제한사항
- 3 ≤ numbers의 길이 ≤ 20
- direction은 "left" 와 "right" 둘 중 하나입니다.


### 입출력 예
|numbers|	kdirection	|result|
|:--|:--|:--|
|[1, 2, 3]|	"right"	|[3, 1, 2]|
|[4, 455, 6, 4, -1, 45, 6]	|"left"	|[455, 6, 4, -1, 45, 6, 4]|

### 입출력 예 설명 1
numbers 가 [1, 2, 3]이고 direction이 "right" 이므로 오른쪽으로 한 칸씩 회전시킨 [3, 1, 2]를 return합니다.


### 입출력 예 설명 2
numbers 가 [4, 455, 6, 4, -1, 45, 6]이고 direction이 "left" 이므로 왼쪽으로 한 칸씩 회전시킨 [455, 6, 4, -1, 45, 6, 4]를 return합니다.
