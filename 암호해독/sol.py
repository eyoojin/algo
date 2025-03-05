def solution(cipher, code):
    answer = list(cipher)
    result = []

    for i in range(1, len(cipher)//code + 1):
        result.append(answer.pop((code-1)*i))
    return ''.join(result)

print(solution("dfjardstddetckdaccccdegk", 4)) # "attack"
print(solution("pfqallllabwaoclk", 2)) # "fallback"