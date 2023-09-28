### 문자열 다루기 기본
***

#### 문제 설명

문자열 str1, str2가 매개변수로 주어집니다. str1 안에 str2가 있다면 1을 없다면 2를 return하도록 solution 함수를 완성해주세요.

##### 제한 조건
1 ≤ str1의 길이 ≤ 100
1 ≤ str2의 길이 ≤ 100

##### 입출력 예

| str1   | str2 | result|
| :--- | :--- |:--- |
| "ab6CDE443fgh22iJKlmn1o"  | 	"6CD"   |1|
| "ppprrrogrammers"  | "pppp"   |2|

##### 입출력 예 #1

"ab6CDE443fgh22iJKlmn1o" str1에 str2가 존재하므로 1을 return합니다.

##### 입출력 예 #2

"ppprrrogrammers" str1에 str2가 없으므로 2를 return합니다.