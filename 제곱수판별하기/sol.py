def solution(n):
    answer = []

    for i in range(1, n):
        answer.append(i ** 2)
    
    if n in answer:
        return 1
    else:
        return 2


print(solution(144)) # 1
print(solution(976)) # 2