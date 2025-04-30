def solution(my_string):
    result = my_string.split()
    answer = int(result[0])
    
    for i in range(len(result)):
        if result[i] == '+':
            answer += int(result[i+1])
        if result[i] == '-':
            answer -= int(result[i+1])
    return answer

print(solution('3 + 4')) # 7