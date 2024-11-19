def count_notebooks(N):
    total_pages=N*1000
    number_of_notebooks=total_pages//100
    return number_of_notebooks
N=int(input().strip())
print(count_notebooks(N))
