def solution(spell, dic):
    answer = 0

    for i in dic:
        if set(spell) == set(i):
            answer +=1
        
    if answer == 1:
        return 1
    else:
        return 2

print(solution(["p", "o", "s"], ["sod", "eocd", "qixm", "adio", "soo"])) # 2
print(solution(["z", "d", "x"], ["def", "dww", "dzx", "loveaw"])) # 1
print(solution(["s", "o", "m", "d"], ["moos", "dzx", "smm", "sunmmo", "som"])) # 2