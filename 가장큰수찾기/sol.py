def solution(array):
    answer = []
    for i in range(len(array)):
        if array[i] == max(array):
            return [max(array), i]
 

print(solution([1, 8, 3])) # [8, 1]
print(solution([9, 10, 11, 8])) # [11, 2]