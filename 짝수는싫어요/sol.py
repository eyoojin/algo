def solution(n):
    answer = []
    for i in range(1, n+1):
        if i % 2 == 1:
            answer.append(i)
    return answer

print(solution(10)) # [1, 3, 5, 7, 9]
print(solution(15)) # [1, 3, 5, 7, 9, 11, 13, 15]