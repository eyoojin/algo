def solution(bin1, bin2):
    answer1 = 0
    answer2 = 0

    result = []
    bin1 = ''.join(reversed(bin1))
    bin2 = ''.join(reversed(bin2))

    for i in range(len(bin1)):
        if bin1[0] == '0':
            answer1 = 0          
        if bin1[0] == '1':
            answer1 = 1

        if i >= 1:
            answer1 += int(bin1[i]) * (2**(i))
    
    for j in range(len(bin2)):
        if bin2[0] == '0':
            answer2 = 0
        if bin2[0] == '1':
            answer2 = 1
            
        if j >= 1:
            answer2 += int(bin2[j]) * (2**(j))
        
    return answer1 + answer2

    # 두번째 if에서 무한반복.,...

print(solution('10', '11')) # 101
print(solution('1001', '1111')) # 11000