def solution(n):
    answer = []

    for i in range(2, n+1):
        if n % i == 0:
            answer.append(i)
            n = n//i
    return answer

print(solution(12)) # [2, 3]
print(solution(17)) # [17]
print(solution(420)) # [2, 3, 5, 7]
print(solution(10000))