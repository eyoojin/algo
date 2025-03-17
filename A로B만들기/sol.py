def solution(before, after):
    answer = 0
    if sorted(before) == sorted(after):
        return 1
    else:
        return 0

print(solution('olleh', 'hello')) # 1
print(solution('allpe', 'apple')) # 0