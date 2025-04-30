def solution(quiz):
    result = []

    for i in quiz:
        x, op, y, eq, z = i.split()
        if op == '-':
            if int(x) - int(y) == int(z):
                result.append('O')
            else:
                result.append('X')
        if op == '+':
            if int(x) + int(y) == int(z):
                result.append('O')
            else:
                result.append('X')
        
    return result

print(solution(["3 - 4 = -3", "5 + 6 = 11"])) 
# ["X", "O"]
print(solution(["19 - 6 = 13", "5 + 66 = 71", "5 - 15 = 63", "3 - 1 = 2"]	)) 
# ["O", "O", "X", "O"]