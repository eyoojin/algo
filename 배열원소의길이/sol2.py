def solution(strlist):
    answer = []

    for i in range(len(strlist)):
        answer.append(len(strlist[i]))
    return answer

print(solution(["We", "are", "the", "world!"])) # [2, 3, 3, 6]
print(solution(["I", "Love", "Programmers."])) # [1, 4, 12]