def solution(dots):
    answer = 0
    a, b = max(dots)
    c, d = min(dots)

    return (a-c) * (b-d)

print(solution([[1, 1], [2, 1], [2, 2], [1, 2]])) # 1
print(solution([[-1, -1], [1, 1], [1, -1], [-1, 1]])) # 4
