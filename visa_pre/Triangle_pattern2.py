def right_angled_triangle(N):
    for i in range(1, N+1):
        for _ in range(i):
            print(i, end=" ")
        print()
N=int(input().strip())
right_angled_triangle(N)
