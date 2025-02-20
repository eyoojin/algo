def solution(array):
    answer = array.sort()
    result = int(len(array)/2)
    return array[result]
    

print(solution([1, 2, 7, 10, 11])) # 7
print(solution([9, -1, 0])) # 0
