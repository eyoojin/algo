def solution(my_string):
    answer = 0

    for char in my_string:
        try: # 문제가 없으면
            answer += int(char)
        except: # 문제가 있으면 except 시도
            continue
            
    return answer        

print(solution("aAb1B2cC34oOp")) # 10
print(solution("1a2b3c4d123")) # 16