from math import sqrt

def solution(n):
    answer = 0

    for num in range(1, int(sqrt(n)) + 1):
        if n % num == 0:
            answer += 2

            if num * num == n:
                answer -= 1

    return answer

print(solution(20)) # 6
print(solution(100)) # 9
