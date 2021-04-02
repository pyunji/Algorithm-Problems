## Q1. [전자레인지](https://www.acmicpc.net/problem/10162)
### [submission](https://www.acmicpc.net/source/27872834)
## Q2. [세탁소 사장 동혁](https://www.acmicpc.net/problem/2720)
### [submission](https://www.acmicpc.net/source/27873213)
## Q3. [캥거루 세마리2](https://www.acmicpc.net/problem/11034)
### [submission](https://www.acmicpc.net/source/27955046)
백준에서 input의 test case 개수가 정해져있지 않을 때  
```python
while 1:
    try:
        # input을 받아 실행할 코드
    except:
        break
```
## Q4. [거스름돈](https://www.acmicpc.net/problem/5585)
### [submission](https://www.acmicpc.net/source/27955470)
## Q5. [컵홀더](https://www.acmicpc.net/problem/2810)
극장의 한 줄에는 자리가 N개가 있다. 서로 인접한 좌석 사이에는 컵홀더가 하나씩 있고, 양 끝 좌석에는 컵홀더가 하나씩 더 있다.   
또, 이 극장에는 커플석이 있다. 커플석 사이에는 컵홀더가 없다.  
극장의 한 줄의 정보가 주어진다. 이때, 이 줄에 사람들이 모두 앉았을 때, 컵홀더에 컵을 꽂을 수 있는 최대 사람의 수를 구하는 프로그램을 작성하시오.  
모든 사람은 컵을 한 개만 들고 있고, 자신의 좌석의 양 옆에 있는 컵홀더에만 컵을 꽂을 수 있다.  

S는 일반 좌석, L은 커플석을 의미하며, L은 항상 두개씩 쌍으로 주어진다.  
어떤 좌석의 배치가 SLLLLSSLL일때, 컵홀더를 *로 표시하면 아래와 같다.
`*S*LL*LL*S*S*LL*`
위의 예에서 적어도 두 명은 컵홀더를 사용할 수 없다.
### [submission](https://www.acmicpc.net/source/27956186)
- S와 LL의 오른쪽(왼쪽)에는 항상 컵홀더가 한 개씩 있다.
    - 좌석의 맨 왼쪽(오른쪽)에는 항상 컵홀더가 한 개 있다.
        - S좌석의 개수 + L좌석의 개수 / 2 + 1 은 컵홀더의 개수이다.
- 컵홀더의 개수는 좌석의 수 N보다 많을 수도 있다.
    - 따라서 컵홀더의 개수와 좌석의 수 중 작은 값이 정답이다.