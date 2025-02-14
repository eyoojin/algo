def solution(n, k):
    eat = 12000 * n
    drink = 2000 * (k - n // 10)

    answer = eat + drink

    return answer

print(solution(10, 3)) # 124000
print(solution(64, 6)) # 768000