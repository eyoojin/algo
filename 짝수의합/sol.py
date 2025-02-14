def solution(n):
    even = range(0, n + 1, 2)
    return sum(even)

print(solution(10)) # 30
# 2 + 4 + 6 + 8 + 10
print(solution(4)) # 6