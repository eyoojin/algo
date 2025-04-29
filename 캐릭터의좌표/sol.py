def solution(keyinput, board):
    [x, y] = board
    x = x//2
    y = y//2
    a = 0
    b = 0

    for i in keyinput:
        if a == x:
            if i == 'right':
                continue
        if a == -x:
            if i == 'left':
                continue
        if b == y:
            if i == 'up':
                continue
        if b == -y:
            if i == 'down':
                continue

        if i == 'right':
            a += 1
        if i == 'left':
            a -= 1
        if i == 'up':
            b += 1
        if i == 'down':
            b -= 1

    return [a, b]
    

print(solution(["left", "right", "up", "right", "right"], [11, 11])) # [2, 1]
print(solution(["down", "down", "down", "down", "down"], [7, 9])) # [0, -4]
print(solution(["right", "right", "right", "right", "right", "left"], [9, 5])) # [3, 0]
