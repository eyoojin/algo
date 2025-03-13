def solution(n):
    for i in range(max(6, n), (6 * n) + 1):
        if i % 6 == 0 and i % n ==0:
            return int(i/6)

# 최소공배수

print(solution(6)) # 1
print(solution(10)) # 5
print(solution(4)) # 2