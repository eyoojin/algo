def solution(n):
    return sum(map(int, list(str(n))))
    #                   list('1234') => ['1', '2', '3', '4']
    #         (map(int())) => [1, 2, 3, 4]
    #      sum()

print(solution(1234)) # 10
print(solution(930211)) # 16