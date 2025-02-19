def solution(my_string):
    answer = list(my_string)
    answer.reverse()

    return ''.join(answer)

print(solution("jaron")) # "noraj"
print(solution("bread")) # "daerb"