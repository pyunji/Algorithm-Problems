s = "A" + input()
 
ans = 0
for i in range(len(s)-1):
    a = abs(ord(s[i])-ord(s[i+1]))
    ans += min(a, 26-a)
print(ans)