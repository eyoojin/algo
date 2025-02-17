def solution(my_string, letter):
    return my_string.replace(letter, '', -1)

print(solution("abcdef", "f")) # "abcde"
print(solution("BCBdbe", "B")) # "Cdbe"