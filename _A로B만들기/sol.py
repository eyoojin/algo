def solution(before, after):
    answer = 0
    for i in before:
        for j in after:
            if i == j:
                answer += 1
    if len(set(after)) != len(after):
        answer -= (len(after) - len(set(after)) + 1)
    if answer == len(after):
        return 1
    else:
        return 0

# 중복되는 문자 처리.......

print(solution('olleh', 'hello')) # 1
print(solution('allpe', 'apple')) # 0