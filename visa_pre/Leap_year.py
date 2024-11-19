def leap_year(year):
    if(year%400==0) or (year%4==0 and year%100!=0):
        return "YES"
    else:
        return "NO"
year=int(input().strip())
print(leap_year(year))
