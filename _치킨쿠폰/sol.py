def solution(chicken):
    answer = 0
    
    a, b = divmod(chicken, 10)
    answer += a
    while a == 0:
        a, b = divmod(a, 10)
        return answer

    # 어려워........

print(solution(100)) # 11
print(solution(1081)) # 120
print(solution(99))