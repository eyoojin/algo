def solution(board):
    answer = []
    li = []
    result = []

    for i in range(0, len(board)):
        for j in range(0, len(board)):
            li.append((i, j))
    
    for i, v in enumerate(board):
        for j, k in enumerate(v):
            if k == 1:
                answer.append((i, j))
    
    for (a, b) in answer:
        result.append((a-1, b-1))
        result.append((a-1, b))
        result.append((a-1, b+1))
        result.append((a, b-1))
        result.append((a, b))
        result.append((a, b+1))
        result.append((a+1, b-1))
        result.append((a+1, b))
        result.append((a+1, b+1))

    return len(set(li) - set(result))
    
    
                
        


print(solution([[0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 1, 0, 0], [0, 0, 0, 0, 0]])) # 16
print(solution([[0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 1, 1, 0], [0, 0, 0, 0, 0]])) # 13
print(solution([[1, 1, 1, 1, 1, 1], [1, 1, 1, 1, 1, 1], [1, 1, 1, 1, 1, 1], [1, 1, 1, 1, 1, 1], [1, 1, 1, 1, 1, 1], [1, 1, 1, 1, 1, 1]])) # 0
