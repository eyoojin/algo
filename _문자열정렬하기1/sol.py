def solution(my_string):
    answer = []
    for i in list(my_string):
        if i in range(0, 10):
            answer.append(i)
    answer.sort()        
    return answer

    # 숫자가 스트링으로 인식돼서 안되는거 같다........

print(solution("hi12392")) # [1, 2, 2, 3, 9]
print(solution("p2o4i8gj2")) # [2, 2, 4, 8]
print(solution("abcde0")) # [0]