t = int(input())
time_set = [300, 60, 10]
if t%10 :
    print(-1)
else:
    button = []
    for time in time_set:
        button.append(str(t//time))
        t = t % time
    print(' '.join(button))