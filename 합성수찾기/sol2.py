def solution(n):
    answer = []

    for i in range(2, n+1):
        for k in range(2, n+1):
            a, b = divmod(i, k)
            if a > 1 and b == 0:
                answer.append(i)

    return len(set(answer))

print(solution(10)) # 5
print(solution(15)) # 8