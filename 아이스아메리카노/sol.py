def solution(money):
    return list(divmod(money, 5500))

print(solution(5500)) # [1, 0]
print(solution(15000)) # [2, 4000]