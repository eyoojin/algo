from math import factorial

def solution(n):
    answer = []

    for i in range(1, 11):
        if factorial(i) <= n:
            answer.append(i)
    return len(answer)

print(solution(3628800)) # 10
print(solution(7)) # 3