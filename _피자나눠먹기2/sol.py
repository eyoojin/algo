def solution(n):
    for a in range(1, 101):
        for k in range(1, 601):
            if (k * 6 / n) == (int(a) == a):
                print(l)
                return k * 6 / n

print(solution(6)) # 1
print(solution(10)) # 5
print(solution(4)) # 2