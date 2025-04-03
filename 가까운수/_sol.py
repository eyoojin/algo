def solution(array, n):
    answer = {}
    result1 = []
    result2 = []

    for i in array:
        if i < n:
            answer[i] = len(range(i, n))
        else:
            answer[i] = len(range(n, i))

    for k, v in answer.items():
        result1.append((k, v))
        result2.append(v)

    for j in range(len(result2)):
        if result1[j][1] == min(result2):
            return result1[j][0]

# 뭐가 틀린거야......

print(solution([3, 10, 28], 20)) # 28
print(solution([10, 11, 12]	, 13)) # 12
