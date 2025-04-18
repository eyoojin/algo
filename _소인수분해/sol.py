def solution(n):
    answer = []
    result = []
    for i in range(2, n+1):
        a, b = divmod(n, i)
        if b == 0:
            answer.append(i)

    return answer

print(solution(12)) # [2, 3]
print(solution(17)) # [17]
print(solution(420)) # [2, 3, 5, 7]