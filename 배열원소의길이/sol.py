def solution(strlist):
    answer = []

    for my_str in strlist:
        answer.append(len(my_str))
    return answer

print(solution(["We", "are", "the", "world!"])) # [2, 3, 3, 6]
print(solution(["I", "Love", "Programmers."])) # [1, 4, 12]