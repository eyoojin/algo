from math import factorial

def solution(n):
    answer = []
    result = []

    for i in range(1, 11):
        fact = factorial(i)
        answer.append(fact)

    for j in answer:
        if j <= n:
            result.append(j)

    return result.index(result[-1]) + 1


print(solution(3628800)) # 10
print(solution(7)) # 3