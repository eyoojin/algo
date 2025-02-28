def solution(order):
    order_list = list(str(order))
    answer = 0
    for i in order_list:
        if i == '3':
            answer += 1
        if i == '6':
            answer += 1    
        if i == '9':
            answer += 1

    return answer

print(solution(3)) # 1
print(solution(29423)) # 2