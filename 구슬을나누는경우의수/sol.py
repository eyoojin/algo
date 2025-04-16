def fact(n):
    if n == 1:
        return 1
    else:
        return n * fact(n-1)

def solution(balls, share):
    return fact(balls) / (fact(share) * fact(balls-share))

print(solution(3, 2)) # 3
print(solution(5, 3)) # 10