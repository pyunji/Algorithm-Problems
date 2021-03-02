#### 여태 python 기초 100제가 아닌 C언어 기초 100제를 풀고 있었다...다시도전.
- 모든 문제를 기록하진 않고, 주목할만한 점이 있는 문제만 기록할 것임
### [Q6007 : [기초-출력] 출력하기07](https://codeup.kr/problem.php?id=6007)
다음 경로를 출력하시오.  

"C:\Download\'hello'.py"  
(단, 따옴표도 함께 출력한다.)
### Answer
```python
print('"C:\Download\\\'hello\'.py"')
```
### [Q6008 : [기초-출력] 출력하기08](https://codeup.kr/problem.php?id=6008)
print("Hello\nWorld")  

위 코드를 정확히 그대로 출력하시오.(공백문자 주의)
### Answer
```python
print('print("Hello\\nWorld")')
```

### [Q6019 : [기초-입출력] 연월일 입력받아 순서 바꿔 출력하기](https://codeup.kr/problem.php?id=6019)
"연도.월.일"을 입력받아 "일-월-연도" 순서로 바꿔 출력해보자.
### Answer
```python
y, m, d = input().split('.')
print(d, m, y, sep='-')     #
```
### [Q6022 : [기초-입출력] 연월일 입력받아 나누어 출력하기(설명)](https://codeup.kr/problem.php?id=6022)
6자리의 연월일(YYMMDD)을 입력받아 나누어 출력해보자.
### Answer
```python
s = input()
for i in range(0, 6, 2):
    print(s[i:i+2], end=' ')    #
```
input
```
960212
```
output
```
96 02 12
```
### [Q6027 : [기초-출력변환] 10진 정수 입력받아 16진수로 출력하기1(설명)](https://codeup.kr/problem.php?id=6027)
### [Q6028 : [기초-출력변환] 10진 정수 입력받아 16진수로 출력하기2(설명)](https://codeup.kr/problem.php?id=6028)
### Answer
```python
print('%x'%n)   # 소문자로 출력
print('%X'%n)   # 대문자로 출력
```
### [Q6029 : [기초-값변환] 16진 정수 입력받아 8진수로 출력하기(설명)](https://codeup.kr/problem.php?id=6029)
### Answer
```python
n = int(input(), 16)    # input을 16진수로 변환
print('%o'%n)
```
### 유니코드 문자 관련 메소드
- `ord()` : 문자 -> 정수값
- `chr()` : 정수값 -> 문자
### [Q6043 : [기초-산술연산] 실수 2개 입력받아 나눈 결과 계산하기](https://codeup.kr/problem.php?id=6043)
- `round(f, n)`: 소숫점 둘째자리 이상의 불필요한 0은 출력되지 않는다.
- 무조건 특정 자리 수 까지 출력해야 하는 경우 print의 서식 문자를 이용하여 출력해야한다.
- `print('%.2f'%n)`: 소숫점 셋째자리에서 반올림 해 둘째자리까지 출력
- `print('%.1f'%n)`: 소숫점 둘째자리에서 반올림 해 첫째자리까지 출력
### [Q6046 : [기초-비트시프트연산] 정수 1개 입력받아 2배 곱해 출력하기](https://codeup.kr/problem.php?id=6046)
정수 1개를 입력받아 2배 곱해 출력해보자.  

*2 를 계산한 값을 출력해도 되지만,  
정수를 2배로 곱하거나 나누어 계산해 주는 비트단위시프트연산자 <<, >>를 이용할 수 있다.  
컴퓨터 내부에는 2진수 형태로 값들이 저장되기 때문에,  
2진수 형태로 저장되어 있는 값들을 왼쪽(<<)이나 오른쪽(>>)으로  
지정한 비트 수만큼 밀어주면 2배씩 늘어나거나 1/2로 줄어드는데,  

왼쪽 비트시프트(<<)가 될 때에는 오른쪽에 0이 주어진 개수만큼 추가되고,  
오른쪽 비트시프트(>>)가 될 때에는 왼쪽에 0(0 또는 양의 정수인 경우)이나 1(음의 정수인 경우)이 개수만큼 추가되고,  
가장 오른쪽에 있는 1비트는 사라진다.  

예시  
n = 10  
print(n<<1)  #10을 2배 한 값인 20 이 출력된다.  
print(n>>1)  #10을 반으로 나눈 값인 5 가 출력된다.  
print(n<<2)  #10을 4배 한 값인 40 이 출력된다.  
print(n>>2)  #10을 반으로 나눈 후 다시 반으로 나눈 값인 2 가 출력된다.  

정수 10의 2진수 표현은 ... 1010 이다.  
10 << 1 을 계산하면 ... 10100 이 된다 이 값은 10진수로 20이다.  
10 >> 1 을 계산하면 ... 101 이 된다. 이 값은 10진수로 5이다.  
### [Q6059 : [기초-비트단위논리연산] 비트단위로 NOT 하여 출력하기](https://codeup.kr/problem.php?id=6059)
#### 음의 정수는 이진법으로 어떻게 표현할까? (보수와 음수)
- [잘 설명되어있는 링크](https://st-lab.tistory.com/189)
- 결론: 어떤 수의 부호를 바꾸고자 한다면 비트를 반전시킨 뒤 1을 더하면 된다.
#### 비트단위(bitwise) 연산자
- ~(bitwise not)
- &(bitwise and)
- |(bitwise or)
- ^(bitwise xor)
- <<(bitwise left shift), >>(bitwise right shift)
### [Q6081 : [기초-종합] 16진수 구구단 출력하기]
A, B, C, D, E, F 중 하나가 입력될 때,  
1부터 F까지 곱한 16진수 구구단의 내용을 출력해보자.  
(단, A ~ F 까지만 입력된다.)  
### Answer
input
```python
n = int(input(), 16)
for i in range(1, 15 + 1):
    print("%X"%n, "*%X"%i, "=%X"%(n*i), sep='')
```
stdout
```
B*1=B
B*2=16
B*3=21
B*4=2C
B*5=37
B*6=42
B*7=4D
B*8=58
B*9=63
B*A=6E
B*B=79
B*C=84
B*D=8F
B*E=9A
B*F=A5
```
### 용량 단위
8 bit(비트)          = 1byte(바이트)       # 8bit=1Byte  
1024 Byte(210 byte) = 1KB(킬로 바이트)  # 1024Byte=1KB  
1024 KB(210 KB)     = 1MB(메가 바이트)  
1024 MB(210 MB)     = 1GB(기가 바이트)  
1024 GB(210 GB)     = 1TB(테라 바이트)  

### [Q6091 : [기초-종합] 함께 문제 푸는 날](https://codeup.kr/problem.php?id=6091)
- 최소공배수 찾기
### Answer
```python
a, b, c = list(map(int, input().split()))
i = 1
while i % a != 0 or i % b != 0 or i % c != 0: #
    i += 1
print(i)
```
### [Q6093 : [기초-리스트] 이상한 출석 번호 부르기2](https://codeup.kr/problem.php?id=6093)

```python
n = int(input())
num_list =list(map(int, input().split()))
for i in range(n-1, -1, -1):    # 거꾸로 포문 돌 때 파라미터 자꾸 헷갈림
    print(num_list[i], end = ' ')
```
### ❗❗ [Q6095 : [기초-리스트] 바둑판에 흰 돌 놓기](https://codeup.kr/problem.php?id=6095)
### Wrong Solution
```python
n = int(input())
axis = []
for _ in range(n):
    axis.append(list(map(int, input().split())))
go = [[0]*19]*19    #
for (i, j) in axis:
    go[i-1][j-1] = 1
```
- `go = [[0]*19]*19`로 빈 2차원 배열을 초기화 할 경우, 각각의 독립적인 객체가 아니라 서로 참조하는 것이 되므로 (1,1)값만 변화시켰는데 1열이 다 변하는 현상 발생
- 즉 모든 행이 복사 붙여넣기 되는 것!
    ```
    [[1, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [1, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [1, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [1, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [1, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [1, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [1, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [1, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [1, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [1, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [1, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [1, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [1, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [1, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [1, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [1, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [1, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [1, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [1, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]]
    ```
- `go = [[0]*19 for _ in range(19)]` 이것은 19번 행을 생성하므로 위의 방식과는 완전히 다르다.
### Answer
```python
go = [[0]*19 for _ in range(19)]    #

n = int(input())

for _ in range(n):
    x, y = list(map(int, input().split()))
    go[x-1][y-1] = 1

for i in go:
    for j in i:
        print(j, end= ' ')
    print(' ')
```
### [Q6096 : [기초-리스트] 바둑알 십자 뒤집기](https://codeup.kr/problem.php?id=6096)
### Answer
```python
go = []
for _ in range(19):
    go.append(list(map(int, input().split())))
n = int(input())
for _ in range(n):
    x, y = list(map(int, input().split()))
    for i in range(0, 19):  ##
        if go[x-1][i]:
            go[x-1][i] = 0
        else:
            go[x-1][i] = 1
        
        if go[i][y-1]:
            go[i][y-1] = 0
        else:
            go[i][y-1] = 1  ##

for i in go:
    for j in i:
        print(j, end= ' ')
    print(' ') 
```
### [Q6097 : [기초-리스트] 설탕과자 뽑기](https://codeup.kr/problem.php?id=6097)
길이가 다른 몇 개의 막대를 바둑판과 같은 격자판에 놓는데,  
격자판의 세로(h), 가로(w), 막대의 개수(n), 각 막대의 길이(l),  
막대를 놓는 방향(d:가로는 0, 세로는 1)과  
막대를 놓는 막대의 가장 왼쪽 또는 위쪽의 위치(x, y)가 주어질 때,  
격자판을 채운 막대의 모양을 출력하는 프로그램을 만들어보자.
### Answer
```python
w, h = list(map(int, input().split()))
grid = [[0] * h for _ in range(w)]
n = int(input())
for _ in range(n):
    l, d, x, y = list(map(int, input().split()))
    for i in range(l):
        if d:
            grid[x-1+i][y-1] = 1
        else:
            grid[x-1][y-1+i] = 1
for i in grid:
    for j in i:
        print(j, end=' ')
    print()
```