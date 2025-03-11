def solution(i, j, k):
    answer = ''
    li = list(map(str, range(i, j+1)))
    for a in li:
        answer += a
       
    return answer.count(str(k))

print(solution(1, 13, 1)) # 6
print(solution(10, 50, 5)) # 5
print(solution(3, 10, 2)) # 0
