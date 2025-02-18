def solution(n):
    answer = 0
    numbers = range(1, 1000001)
    for i in numbers:
        if n % i == 0:
            answer += 1

    return answer

print(solution(20)) # 6
print(solution(1000000)) # 9


