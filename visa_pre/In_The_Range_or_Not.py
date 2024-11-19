def binary_hear(T, frequencies):
    for X in frequencies:
        if 67 <= X <= 45000:
            print("YES")
        else:
            print("NO")
T=int(input())
frequencies=[int(input()) for _ in range(T)]
binary_hear(T, frequencies)
