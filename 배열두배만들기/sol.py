def solution(numbers):
    answer = []
    def double(x):
        return x * 2
    answer = list(map(double, numbers))
    return answer

print(solution([1, 2, 3, 4, 5])) # [2, 4, 6, 8, 10]
print(solution([1, 2, 100, -99, 1, 2, 3])) # [2, 4, 200, -198, 2, 4, 6]