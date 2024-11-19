T=int(input())
for _ in range(T):
    X,N=map(int, input().split())
    points_for_each_test_case=X//10
    score=points_for_each_test_case*N
    print(score)
