def solution(n):
    answer = 0

    for i in str(n):
        answer = answer + int(i)

    return answer

print(solution(1234)) # 10
print(solution(930211)) # 16