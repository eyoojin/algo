def solution(array):
    answer = []
    result = []

    for i in array:
        answer.append(array.count(i))
    for j in array:
        if array.count(j) == max(answer):
            result.append(j)
    if len(set(result)) == 1:
        return result[0]
    else:
        return -1
        

print(solution([1, 2, 3, 3, 3, 4])) # 3
print(solution([1, 1, 2, 2])) # -1
print(solution([1])) # 1