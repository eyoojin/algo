def solution(my_string):
    answer = ''
    for i in range(len(my_string)):
        for j in range(1, len(my_string)):
            if my_string[i] == my_string[j]:
                answer += my_string[i]

    return my_string

print(solution("people")) # "peol"
print(solution("We are the world")) # "We arthwold"