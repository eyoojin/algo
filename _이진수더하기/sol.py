def solution(bin1, bin2):
    answer1 = 0
    answer2 = 0
    result = []
    bin1 = ''.join(reversed(bin1))
    bin2 = ''.join(reversed(bin2))

    for i in range(len(bin1)):
        answer1 += int(bin1[i]) * (2**(i))
    
    for j in range(len(bin2)):
        answer2 += int(bin2[j]) * (2**(j))

    answer = answer1 + answer2

    for i in range(10):
        if answer >= 2**i and answer < 2**(i+1):
            for k in range(i):
                answer, b = divmod(answer, 2)
                result.append(b)

    result.append(answer)
    result = list(map(str, result))

    return ''.join(reversed(result))

    # why...........

print(solution('10', '11')) # 101
print(solution('1001', '1111')) # 11000