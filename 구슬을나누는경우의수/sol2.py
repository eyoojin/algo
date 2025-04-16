def fact(n):
    answer = 1
    for i in range(1, n+1):
        answer *= i
    return answer

def solution(balls, share):
    return fact(balls) / (fact(share) * fact(balls-share))


# for문으로 변경

print(solution(3, 2)) # 3
print(solution(5, 3)) # 10