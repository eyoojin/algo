def solution(s):
    answer = []
    slist = s.split()

    for i in range(len(slist)):
        if slist[i] == 'Z':
            answer.append(i)
    
    if len(answer) == 0:
        return sum(map(int, slist))
    else:
        for j in reversed(answer):
            slist.pop(j)
            slist.pop(j-1)
        return sum(map(int, slist))
            



print(solution("1 2 Z 3")) # 4
print(solution("10 20 30 40")) # 100
print(solution("10 Z 20 Z 1")) # 1
print(solution("10 Z 20 Z")) # 0
print(solution("-1 -2 -3 Z")) # -3
