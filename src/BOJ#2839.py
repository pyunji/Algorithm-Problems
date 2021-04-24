n = int(input())
if n <= 10:
    if n%3==0:
        ans = n//3
    elif n%5==0:
        ans = n//5
    elif n==8:
        ans = 2
    else:
        ans = -1
else:
    if n%5==0:
        ans = n//5
    elif (n%5)%2==0:
        ans = 2 + (n//5)
    else:
        ans = 1 + (n//5)
print(ans)