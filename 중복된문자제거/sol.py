def solution(my_string):
    result = []
    for i in my_string:
        if i not in result:
            result.append(i)

    return ''.join(result)

print(solution("people")) # "peol"
print(solution("We are the world")) # "We arthwold"