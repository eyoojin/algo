def solution(my_string):
    my_list = list(str(my_string))
    numbers = list(map(str, range(1, 10)))

    result = []

    for number in my_string:
        if number in numbers:
            result.append(number)
    list_int = list(map(int, result))   
    
    return sum(list_int)


print(solution("aAb1B2cC34oOp")) # 10
print(solution("1a2b3c4d123")) # 16



