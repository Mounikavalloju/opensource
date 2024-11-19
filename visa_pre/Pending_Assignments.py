x,y,z=map(int, input().split())
total_time=2*24*60
total_time_needed=x*y
if total_time_needed<=total_time:
    print("YES")
else:
    print("NO")
