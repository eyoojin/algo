def solution(chicken):
  
    a, b = divmod(chicken, 10)
    answer = a
    coupon = a + b

    while coupon >= 10:
        a, b = divmod(coupon, 10)
        answer += a
        coupon = a + b
    
    return answer

print(solution(100)) # 11
print(solution(1081)) # 120
print(solution(99))