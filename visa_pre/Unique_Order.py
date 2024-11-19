def unique_order(arr):
    seen=set()
    result = []
    for num in arr:
        if num not in seen:
            result.append(num)
            seen.add(num)
    return result
N=int(input())
arr=list(map(int, input().split()))
unique_arr=unique_order(arr)
print(" ".join(map(str, unique_arr)))
