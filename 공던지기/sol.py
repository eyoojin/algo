def solution(numbers, k):
    answer = []
    a , b = divmod(k*2-1, len(numbers))
    for i in range(a+1):
        answer.append(numbers)
    
    return answer[a][b-1]

    
    
    

print(solution([1, 2, 3, 4], 2)) # 3
print(solution([1, 2, 3, 4, 5, 6], 5)) # 3
print(solution([1, 2, 3], 3)) # 2
