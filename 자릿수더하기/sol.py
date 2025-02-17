def solution(n):
    list_str = list(str(n))
    list_int = list(map(int, list_str))
    return sum(list_int)

print(solution(1234)) # 10
print(solution(930211)) # 16