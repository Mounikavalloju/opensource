def right_angled_triangle(N):
    current_num=1
    for row in range(1, N+1):
        for i in range(row):
            print(current_num, end=" ")
            current_num+=1
        print()
N=int(input().strip())
right_angled_triangle(N)
