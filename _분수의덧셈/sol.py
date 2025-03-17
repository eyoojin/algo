def solution(numer1, denom1, numer2, denom2):
    answer = []
    for i in range(max(denom1, denom2), denom1*denom2+1):
        if i % denom1 == 0 and i % denom2 == 0:
            answer.append(i)

    denom = min(answer)
    numer = numer1 * (denom/denom1) + numer2 * (denom/denom2)
    return [int(numer), denom]
    

print(solution(1, 2, 3, 4)) # [5, 4]
print(solution(9, 2, 1, 3)) # [29, 6]