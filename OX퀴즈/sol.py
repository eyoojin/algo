def solution(quiz):
    result = []

    for i in quiz:
        answer = i.split()
        for j in range(len(answer)):
            if answer[j] == '-':
                sol = int(answer[j-1]) - int(answer[j+1])
                if sol == int(answer[-1]):
                    result.append('O')
                else:
                    result.append('X')
            if answer[j] == '+':
                sol = int(answer[j-1]) + int(answer[j+1])
                if sol == int(answer[-1]):
                    result.append('O')
                else:
                    result.append('X')

    return result

print(solution(["3 - 4 = -3", "5 + 6 = 11"])) 
# ["X", "O"]
print(solution(["19 - 6 = 13", "5 + 66 = 71", "5 - 15 = 63", "3 - 1 = 2"]	)) 
# ["O", "O", "X", "O"]