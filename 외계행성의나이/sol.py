def solution(age):
    answer = list(str(age))
    words = 'abcdefghij'
    for i in range(len(answer)):
        answer[i] = words[int(answer[i])]
    
    return ''.join(answer)

print(solution(23)) # cd
print(solution(51)) # fb
print(solution(100)) # baa 

print(solution(1000)) # 