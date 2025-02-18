from math import ceil

def solution(slice, n):
    if n // slice >= 1:
        return ceil(n // slice)

print(solution(7, 10)) # 2
print(solution(4, 12)) # 3