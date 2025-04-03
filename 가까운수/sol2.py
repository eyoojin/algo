def solution(array, n):
    answer = []
    result = []

    for i in array:
        answer.append(abs(i-n))

    if answer.count(min(answer)) == 1:
        return array[answer.index(min(answer))]
    else:
        for j, k in enumerate(answer):
            if min(answer) == k:
                result.append(array[j])
        return min(result)
            




print(solution([3, 10, 28], 20)) # 28
print(solution([10, 11, 12]	, 13)) # 12
print(solution([1, 3, 4], 2))