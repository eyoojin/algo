def solution(my_string):
    answer = 0

    for char in my_string:      
        if not (ord('A') <= ord(char) <= ord('z')): # 아스키코드
            answer += int(char)

    return answer

print(solution("aAb1B2cC34oOp")) # 10
print(solution("1a2b3c4d123")) # 16