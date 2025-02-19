from math import ceil

def solution(slice, n):
    return ceil(n / slice)

print(solution(7, 10)) # 2
print(solution(4, 12)) # 3