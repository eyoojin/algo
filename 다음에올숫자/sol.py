def solution(common):
    answer = 0
    if common[2] - common[1] == common[1] - common[0]:
        answer = common[-1] + (common[1] - common[0])

    else:
        answer = common[-1] * (common[1] // common[0])
    return answer

print(solution([1, 2, 3, 4])) # 5
print(solution([2, 4, 8])) # 16