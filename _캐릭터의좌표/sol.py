def solution(keyinput, board):
    [x, y] = board
    x = int(x/2)
    y = int(y/2)
    a = keyinput.count('right')
    b = keyinput.count('left')
    c = keyinput.count('up')
    d = keyinput.count('down')

    if a > x:
        for i in range(a-x):
            keyinput.remove('right')
    if b > x:
        for i in range(b-x):
            keyinput.remove('left')
    if c > y:
        for i in range(c-y):
            keyinput.remove('up')
    if d > y:
        for i in range(d-y):
            keyinput.remove('down')
    
    a = keyinput.count('right')
    b = keyinput.count('left')
    c = keyinput.count('up')
    d = keyinput.count('down')
    
    return [a-b, c-d]

print(solution(["left", "right", "up", "right", "right"], [11, 11])) # [2, 1]
print(solution(["down", "down", "down", "down", "down"], [7, 9])) # [0, 4]
print(solution(["right", "right", "right", "right", "right", "left"], [9, 5])) # [3, 0]
