#### 여태 python 기초 100제가 아닌 C언어 기초 100제를 풀고 있었다...다시도전.
- 모든 문제를 기록하진 않고, 주목할만한 점이 있는 문제만 기록할 것임
### [Q6007 : [기초-출력] 출력하기07](https://codeup.kr/problem.php?id=6007)
다음 경로를 출력하시오.  

"C:\Download\'hello'.py"  
(단, 따옴표도 함께 출력한다.)
### A6007
```python
print('"C:\Download\\\'hello\'.py"')
```
### [Q6008 : [기초-출력] 출력하기08](https://codeup.kr/problem.php?id=6008)
print("Hello\nWorld")  

위 코드를 정확히 그대로 출력하시오.(공백문자 주의)
### A6008
```python
print('print("Hello\\nWorld")')
```

### [Q6019 : [기초-입출력] 연월일 입력받아 순서 바꿔 출력하기](https://codeup.kr/problem.php?id=6019)
"연도.월.일"을 입력받아 "일-월-연도" 순서로 바꿔 출력해보자.
### A6019
```python
y, m, d = input().split('.')
print(d, m, y, sep='-')
```
