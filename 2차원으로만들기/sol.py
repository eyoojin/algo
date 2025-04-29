import numpy as np

def solution(num_list, n):
    k = int(len(num_list) / n)
    answer = np.array(num_list).reshape(k, n)
    return answer.tolist()

print(solution([1, 2, 3, 4, 5, 6, 7, 8], 2)) 
# [[1, 2], [3, 4], [5, 6], [7, 8]]
print(solution([100, 95, 2, 4, 5, 6, 18, 33, 948], 3)) 
# [[100, 95, 2], [4, 5, 6], [18, 33, 948]]