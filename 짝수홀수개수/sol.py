def solution(num_list):
    even = []
    odd = []
    for num in num_list:
        if num % 2 == 0:
            even.append(num)
        else:
            odd.append(num)

    return [len(even), len(odd)]

    
print(solution([1, 2, 3, 4, 5])) # [2, 3]
print(solution([1, 3, 5, 7])) # [0, 4]