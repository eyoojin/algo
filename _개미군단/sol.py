def solution(hp):
    while hp >= 0:

        if hp % 5 == 0:
            return hp // 5
        elif (hp % 5) % 3 == 0:
            return hp // 5 + (hp % 5) // 3
        else:
            return hp // 5 + (hp % 5) // 3 + ((hp % 5) % 3) // 1
        

print(solution(23)) # 5
print(solution(24)) # 6
print(solution(999)) # 201



