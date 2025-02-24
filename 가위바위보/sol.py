def solution(rsp):
    answer = []
    
    for i in list(rsp):
        
        if i == '2':
            answer.append('0')
        elif i == '0':
            answer.append('5')
        elif i == '5':
            answer.append('2')
        
    return ''.join(answer)
    

print(solution('2')) # '0'
print(solution('205')) # '052'