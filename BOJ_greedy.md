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
## ❗ Q6. [한조서열정리](https://www.acmicpc.net/problem/14659)
### [submission](https://www.acmicpc.net/source/28090605)
- 내가 제출했던 수많은 비효율적인 코드를 확인하기
- 내가 약한 부류의 문제임
    - 가장 높은 값이 나올때까지 1을 더하면 되는데 투포인터로 푸는 것이 잘못되었음.

## Q7. [ZOAC 2](https://www.acmicpc.net/problem/18238)
### [submission](https://www.acmicpc.net/source/28091947)

## Q8. [책 정리] (https://www.acmicpc.net/problem/1434)
### [submission] (https://www.acmicpc.net/source/28126642)
- 맨 처음엔 이렇게 풀었는데, 마지막 루프가 돌고나서 한번 더 돌게 하는 방법을 찾지 못해서 틀렸었음.
```python
from collections import deque
n, m = list(map(int, input().split()))
a = deque(list(map(int, input().split())))
b = deque(list(map(int, input().split())))
ans = 0

box = a.popleft()
book = b.popleft()
# print(a, b, type(box), type(book))
# book()
while a or b:
    print(a, b, box, book)
    if box < book:
        ans += box
        box = a.popleft()
    else:
        box = box - book
        book = b.popleft()    
print(ans)
```
- `while True`, `try-except` 문을 활용하여 deque가 비어있을 경우 에러를 처리함과 동시에 남은 연산도 수행해주었음
```python
from collections import deque
# n, m = list(map(int, input().split()))
input()
a = deque(list(map(int, input().split())))
b = deque(list(map(int, input().split())))
ans = 0

box = a.popleft()
book = b.popleft()

try:
    while True:
        print(a, b, box, book)
        if box < book:
            ans += box
            box = a.popleft()
        else:
            box = box - book
            book = b.popleft()    
except:
    ans += box
    pass
ans += sum(a)
ans
```
```
메모리 32676kb
시간 116ms
```
- deque를 import해서 실행할 시 메모리와 시간을 좀 더 잡아먹게 된다고 판단하여 그냥 list로 사용
    - `List().pop(0)`보다 `deque().popleft()`가 빠르다고 들었는데..
```python
# from collections import deque
input()
a = list(map(int, input().split()))
b = list(map(int, input().split()))
ans = 0

box = a.pop(0)
book = b.pop(0)

try:
    while True:
        if box < book:
            ans += box
            box = a.pop(0)
        else:
            box = box - book
            book = b.pop(0)
except:
    ans += box
    pass
ans += sum(a)
print(ans)
```
```
메모리 28776kb
시간 68ms
```