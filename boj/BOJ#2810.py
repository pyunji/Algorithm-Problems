from collections import Counter
n = int(input())
c = Counter(input())
print(min((c['S']+c['L']//2+1), n))