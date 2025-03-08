def solution(num, k):
    for i in range(len(str(num))):
        if str(k) == str(num)[i]:
            return i + 1
        if str(k) not in list(str(num)):
            return -1

print(solution(29183, 1)) # 3
print(solution(232443, 4)) # 4
print(solution(123456, 7)) # -1