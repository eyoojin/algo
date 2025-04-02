def solution(chicken):
  
    a, b = divmod(chicken, 10)
    answer = a
    remainder = b

    while a >= 10:
        a, b = divmod(a, 10)
        answer += a
        remainder += b
    
    remainder += a
    
    if remainder >= 10:
        return remainder//10 + answer
    
    return answer

    # 어려워........

print(solution(100)) # 11
print(solution(1081)) # 120
print(solution(99))