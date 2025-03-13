def solution(emergency):
    answer = []
    li = sorted(emergency, reverse=True)

    for i in emergency:
        for j in range(len(li)):
            if i == li[j]:
                answer.append(j+1)
    
    return answer

print(solution([3, 76, 24])) # [3, 1, 2]
print(solution([1, 2, 3, 4, 5, 6, 7])) # [7, 6, 5, 4, 3, 2, 1]
print(solution([30, 10, 23, 6, 100])) # [2, 4, 3, 5, 1]