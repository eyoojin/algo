def solution(numlist, n):
    answer = []
    result = {}

    for i in numlist:
        result[i] = abs(n-i)


    return result


print(solution([1, 2, 3, 4, 5, 6], 4)) # [4, 5, 3, 6, 2, 1]
print(solution([10000,20,36,47,40,6,10,7000], 30)) # [36, 40, 20, 47, 10, 6, 7000, 10000]
