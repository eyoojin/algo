def solution(n):
    answer = []
    result = []

    for j in range(2, n+1):
        if n % j == 0:
            result.append(j)
            n = n//j

    for i in result:
        for k in result:
            a, b = divmod(i, k)
            if a > 1 and b == 0:
                answer.append(i)
    sol = list(set(result) - set(answer))
    sol.sort()
    return sol

print(solution(12)) # [2, 3]
print(solution(17)) # [17]
print(solution(420)) # [2, 3, 5, 7]
print(solution(3204))
print(solution(10000))