def solution(numbers):
    numbers.sort()
    if numbers[0] * numbers[1] > numbers[-2] * numbers[-1]:
        return numbers[0] * numbers[1]
    else:
        return numbers[-2] * numbers[-1]
    

print(solution([1, 2, -3, 4, -5])) # 15
print(solution([0, -31, 24, 10, 1, 9])) # 240
print(solution([10, 20, 30, 5, 5, 20, 5])) # 600