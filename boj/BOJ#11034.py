while True:
    try:
        a, b, c = list(map(int, input().split()))

        print((b-a if (b-a)>(c-b) else c-b) - 1)
    except:
        break