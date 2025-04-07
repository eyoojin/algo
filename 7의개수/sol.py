def solution(array):
    answer = 0
    
    for i in array:
        answer += list(str(i)).count('7')
        
    return answer
            

print(solution([7, 77, 17])) # 4
print(solution([10, 29])) # 0
