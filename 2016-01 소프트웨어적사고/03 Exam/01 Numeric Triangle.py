def ntriangle(k):
    n = 1
    for i in range(k):
        for j in range(i+1):
            print(n, end=' ')
            n += 1
        print()

ntriangle(int(input("k=")))