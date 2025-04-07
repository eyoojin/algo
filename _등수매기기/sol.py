def solution(score):
    answer = list(map(sum, score))

    for i in range(1, len(answer)+1):
        if answer.count(max(answer)) > 1:
            for j in range(answer.count(max(answer))):
                answer[answer.index(max(answer))] = i
              
        else:
            answer[answer.index(max(answer))] = i

    return answer

print(solution([[80, 70], [90, 50], [40, 70], [50, 80]])) # [1, 2, 4, 3]
print(solution([[80, 70], [70, 80], [30, 50], [90, 100], [100, 90], [100, 100], [10, 30]])) # [4, 4, 6, 2, 2, 1, 7]

