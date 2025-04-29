def solution(num_list, n):
    answer = []
    for i in range(len(num_list)//n):
        answer.append([0])
    
    


    
    return answer

print(solution([1, 2, 3, 4, 5, 6, 7, 8], 2)) 
# [[1, 2], [3, 4], [5, 6], [7, 8]]
print(solution([100, 95, 2, 4, 5, 6, 18, 33, 948], 3)) 
# [[100, 95, 2], [4, 5, 6], [18, 33, 948]]