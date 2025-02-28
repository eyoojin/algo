def solution(my_string):
    my_string = my_string.lower()
    answer = list(my_string)
    answer.sort()
    return ''.join(answer)

print(solution("Bcad")) # "abcd"
print(solution("heLLo")) # "ehllo"
print(solution("Python")) # "hnopty"