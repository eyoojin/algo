def solution(n):
    prime = {1, 2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97}
    answer = set(range(1, n+1))
    return len(answer-prime)

    # 소수를 골라내면 될 거 같은데.....

print(solution(10)) # 5
print(solution(15)) # 8
