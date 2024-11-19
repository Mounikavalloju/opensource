def reverse_integer(n):
    sign=-1 if n<0 else 1
    n=abs(n)
    reversed_num=int(str(n)[::-1]) *sign
    if reversed_num<-2**31 or reversed_num>2**31-1:
        return 0
    return reversed_num
n=int(input())
print(reverse_integer(n))
