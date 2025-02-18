def solution(numbers):
    numbers.sort() # 오름차순 정렬
    return numbers[-1] * numbers[-2]
    

print(solution([1, 2, 3, 4, 5])) # 20
print(solution([0, 31, 24, 10, 1, 9])) # 744