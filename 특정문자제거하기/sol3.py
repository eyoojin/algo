def solution(my_string, letter):
    answer = '' # 비어있는 문자열

    for char in my_string:
        if char != letter: # 특정문자 골라내기
            answer = answer + char # concetenation

    return answer

print(solution("abcdef", "f")) # "abcde"
print(solution("BCBdbe", "B")) # "Cdbe"