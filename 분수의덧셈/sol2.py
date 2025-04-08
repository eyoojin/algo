def solution(numer1, denom1, numer2, denom2):
    answer = []
    result = []

    numer = numer1 * denom2 + numer2 * denom1
    denom = denom1 * denom2

    for j in range(min(numer, denom), 0, -1):
        if numer % j == 0 and denom % j == 0:
            result.append(j)
    result = max(result)
    
    return [int(numer/result), int(denom/result)]
    

print(solution(1, 2, 3, 4)) # [5, 4]
print(solution(9, 2, 1, 3)) # [29, 6]
print(solution(2, 4, 2, 4))
print(solution(2, 4, 1, 2))