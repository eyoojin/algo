def solution(my_string):
    answer = 0

    for i in list(my_string):
        if i == int(i):
            answer += int(i)

    return answer

print(solution('aAb1B2cC34oOp')) # 37
print(solution('1a2b3c4d123Z')) # 133
