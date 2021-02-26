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