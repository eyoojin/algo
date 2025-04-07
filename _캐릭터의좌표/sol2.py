def solution(keyinput, board):
    [x, y] = board
    x = int(x/2)
    y = int(y/2)
    a = 0
    c = 0

    for i in keyinput:
        if i == 'right':
            a += 1
            if a == x:
                a = x
        if i == 'left':
            a -= 1
            if a == -x:
                a = -x
        if i == 'up':
            c += 1
            if c == y:
                c = y
        if i == 'down':
            c -= 1
            if c == -y:
                c = -y
    return [a, c]