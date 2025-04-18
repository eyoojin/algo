def solution(num, total):
    answer = []

    if num == 1:
        return [total]

    if num % 2 == 1:
        for i in range(1, num//2+1):
            answer.append(total//num)
            answer.append(total//num-i)
            answer.append(total//num+i)
        answer = set(answer)
        answer = list(answer)
        answer.sort()
    if num % 2 == 0:
        for j in range(1, num//2+1):
            answer.append(total//num)
            answer.append(total//num-j)
            answer.append(total//num+j)
        answer = set(answer)
        answer = list(answer)
        answer.sort()
        answer.pop(0)
    return answer

print(solution(3, 12)) # [3, 4, 5]
print(solution(5, 15)) # [1, 2, 3, 4, 5]
print(solution(4, 14)) # [2, 3, 4, 5]
print(solution(5, 5)) # [-1, 0, 1, 2, 3]
print(solution(1, 0))