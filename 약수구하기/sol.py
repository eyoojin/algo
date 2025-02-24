def solution(n):
    answer = []
    for i in range(1, n+1):
        if n % i == 0:
            answer.append(i)

    return answer

print(solution(24)) # [1, 2, 3, 4, 6, 8, 12, 24]
print(solution(29)) # [1, 29]