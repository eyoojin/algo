def solution(n, t):
    answer = n * (2 ** t)
    return answer

print(solution(2, 10)) # 2048
print(solution(7, 15)) # 229376