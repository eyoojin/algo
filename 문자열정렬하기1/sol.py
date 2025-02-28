def solution(my_string):
    answer = []
    for i in list(my_string):
        if i in list('0123456789'):
            answer.append(i)
        answer = list(map(int, answer)) 
    answer.sort()
    
    return answer

print(solution("hi12392")) # [1, 2, 2, 3, 9]
print(solution("p2o4i8gj2")) # [2, 2, 4, 8]
print(solution("abcde0")) # [0]