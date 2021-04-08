n = int(input())
heights = list(map(int, input().split()))
 
cnt = 0
cnt_max = 0
max_height = 0
 
for height in heights:
    if height > max_height:
        max_height = height
        cnt = 0
    else:
        cnt += 1
    cnt_max = max(cnt, cnt_max)
    
print(cnt_max)