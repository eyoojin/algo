def solution(array, height):
    answer = 0

    for i in range(len(array)):
        if array[i] > height:
            answer += 1
    return answer

print(solution([149, 180, 192, 170], 167)) # 3
print(solution([180, 120, 140], 190)) # 0