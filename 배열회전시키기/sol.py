def solution(numbers, direction):
    answer = []
    if direction == 'right':
        answer.append(numbers[-1])
        for i in range(len(numbers)-1):
            answer.append(numbers[i])
    else:
        answer.append(numbers[1])
        for j in range(2, (len(numbers))):
            answer.append(numbers[j])
        answer.append(numbers[0])

    return answer

print(solution([1, 2, 3], 'right')) # [3, 1, 2]
print(solution([4, 455, 6, 4, -1, 45, 6], 'left')) # [455, 6, 4, -1, 45, 6, 4]