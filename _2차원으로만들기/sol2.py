def solution(num_list, n):
    answer = []
    for i in num_list:
        answer.append([i])
    return answer

print(solution([1, 2, 3, 4, 5, 6, 7, 8], 2)) 
# [[1, 2], [3, 4], [5, 6], [7, 8]]
print(solution([100, 95, 2, 4, 5, 6, 18, 33, 948], 3)) 
# [[100, 95, 2], [4, 5, 6], [18, 33, 948]]