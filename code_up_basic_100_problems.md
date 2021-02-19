### [Q1001. [기초-출력] 출력하기01](https://codeup.kr/problem.php?id=1001)
```python
print("Hello")
```
### [Q1002. [기초-출력] 출력하기02](https://codeup.kr/problem.php?id=1002)
```python
print("Hello World")
```
### [Q1003. [기초-출력] 출력하기03](https://codeup.kr/problem.php?id=1003)
```python
print("Hello\nWorld")
```
```python
print("""Hello
World""")
```
### [Q1004. [기초-출력] 출력하기04](https://codeup.kr/problem.php?id=1004)
```python
print("\'Hello\'")
```
### [Q1005. [기초-출력] 출력하기05](https://codeup.kr/problem.php?id=1005)
```python
print('\"Hello World\"')
```
### [Q1006. [기초-출력] 출력하기06](https://codeup.kr/problem.php?id=1006)
```python
print('"!@#$%^&*()"')
```
stdout
```
"!@#$%^&*()"
```
### [Q1007. [기초-출력] 출력하기07](https://codeup.kr/problem.php?id=1007)
```python
print('"C:\Download\hello.cpp"')
```
```python
print("\"C:\\Download\\hello.cpp\"")
```
stdout
```
"C:\Download\hello.cpp"
```
### [Q1008. [기초-출력] 출력하기08](https://codeup.kr/problem.php?id=1008)
```python
print("\u250C\u252C\u2510\n\
\u251C\u253C\u2524\n\
\u2514\u2534\u2518")
```
stdout
```
┌┬┐
├┼┤
└┴┘
```
### [Q1010. [기초-입출력] 정수 1개 입력받아 그대로 출력하기](https://codeup.kr/problem.php?id=1010)
```python
print(input())
```
### [Q1011. [기초-입출력] 문자 1개 입력받아 그대로 출력하기](https://codeup.kr/problem.php?id=1011)
```python
print(input())
```
### [Q1012. [기초-입출력] 실수 1개 입력받아 그대로 출력하기](https://codeup.kr/problem.php?id=1012)
```python
n = float(input())
print("%6f" %n)
```
### [Q1013. [기초-입출력] 정수 2개 입력받아 그대로 출력하기](https://codeup.kr/problem.php?id=1013)
```python
print(input())
```
### [Q1014. [기초-입출력] 문자 2개 입력받아 순서 바꿔 출력하기](https://codeup.kr/problem.php?id=1014)
```python
a, _, b = input()
print(b, a)
```
### [Q1015. [기초-입출력] 실수 입력받아 둘째 자리까지 출력하기](https://codeup.kr/problem.php?id=1015)
```python
n = float(input())
print("%.2f" %n)
```
### [Q1017. [기초-입출력] 정수 1개 입력받아 3번 출력하기](https://codeup.kr/problem.php?id=1017)
```python
n = input()
print(n, n, n)
```
### [Q1018. [기초-입출력] 시간 입력받아 그대로 출력하기](https://codeup.kr/problem.php?id=1018)
```python
print(input())
```
### [Q1019. [기초-입출력] 연월일 입력받아 그대로 출력하기](https://codeup.kr/problem.php?id=1019)
### A1019_1. 정수로 받은 후 format함수
```python
a, b, c = list(map(int, input().split('.')))
print("{0:04d}.{1:02d}.{2:02d}".format(a, b, c))
```
### A1019_2. zfill사용해 스트링 왼쪽에 zero 채우기
- 왠지 통과는 안되는데 중요함
```python
a, b, c = input().split('.')
print(f"{a}.{b.zfill(2)}.{c.zfill(2)}")
```
### A1019_3. rjust사용해 스트링 자리 채우기
- 왠지 통과는 안되는데 중요함
```python
a, b, c = input().split('.')
print(f"{a}.{b.rjust(2, '0')}.{c.rjust(2, '0')}")
```

```python
a, b = input().split('-')
print(a + b)
```
### [Q1020. [기초-입출력] 주민번호 입력받아 형태 바꿔 출력하기](https://codeup.kr/problem.php?id=1019)
```python
a, b = input().split('-')
print(a + b)
```
### [Q1021. [기초-입출력] 단어 1개 입력받아 그대로 출력하기(설명)](https://codeup.kr/problem.php?id=1021)
```python
print(input())
```
### [Q1022. [기초-입출력] 문장 1개 입력받아 그대로 출력하기(설명)](https://codeup.kr/problem.php?id=1022)
```python
print(input())
```