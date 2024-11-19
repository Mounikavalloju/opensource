def maximum_mangoes(X,Y,Z):
    remaining_weight=Z-Y
    if remaining_weight<0:
        return 0
    max_mangoes=remaining_weight//X
    return max_mangoes
X,Y,Z=map(int, input().split())
print(maximum_mangoes(X,Y,Z))
