def solution(n):
    for k in range(1, 601):
        if n * k / 6 >= 1:
            return k


print(solution(6)) # 1
print(solution(10)) # 5
print(solution(4)) # 2