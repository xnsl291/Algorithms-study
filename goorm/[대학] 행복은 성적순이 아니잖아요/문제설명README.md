## 행복은 성적순이 아니잖아요
***

### 문제 설명

구름 대학교에서 재학중인 구름이는, 오늘도 자신의 성적을 올리기 위해서 도서관에서 앉아 공부를 하고 있다. 그러던 도중, 한 도인이 구름이에게 다가와 말을 했다. "구름아, 행복은 성적순이 아니란다. 등수는 조금 낮아도 A+만 받으면 상관없단다." 이 말을 들은 구름이는 큰 깨달음을 얻고 1등을 하기 보다는 모든 과목에서 A+를 받는것을 이번학기의 목표로 바꾸었다.

구름 대학에서 A+을 받는것은 매우 어렵다. 시험 성적이 전체 학생에서 n%보다 높은 백분위를 가지고 있어야 하고, 성적이 좋더라도 k개의 수행평가 중 하나라도 m점보다 낮거나 같으면 A+를 받을 수 없다.

구름이가 이번 학기 t개의 수업을 듣고, 모든 성적이 나왔다, 과연 구름이는 모든 과목에서 A+를 받았는지 확인해보자 

### 입력
≤
- 첫번째 줄에 구름이가 듣는 수업의 개수 t (1 ≤ t ≤ 20 ) 이 주어진다
- 두번째 줄부터 t줄동안 각 과목별 전체 학생 수 l (1≤ l ≤ 10,000), 구름이의 등수 s (1 ≤ s ≤ 100), 과목의 수행 평가의 개수 k (1 ≤ k ≤ 1,000), A+과목의 수행 평가의 과락 점수의 기준인 점수 m (1 ≤ m ≤ 100)과 구름이가 받은 수행평가 점수 Vi가 k개가 모두 공백을 두고 주어진다. 각 수행평가 점수는 1이상 100 이하의 정수이다 
 
<br>

### 출력
구름이가 모든 과목에서 A+을 받았는지 확인하고 모든 과목에서 A+이라면 1을 출력하고 아니라면 0을 출력하세요 

### 입출력예시
### 예시1 

#### 입력
```
1
100 9 10 3 10 11 15 20
```
#### 출력
```
1
```
<br>

### 예시2 
#### 입력
```
2
100 9 10 3 10 11 15 20
100 21 20 3 20 21 22 23
```
#### 출력
```
0
```
