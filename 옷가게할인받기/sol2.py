def solution(price):
    answer = 0
    if price >= 500000:
        return int(price * 0.80)
    elif price >= 300000:
        return int(price * 0.90)
    elif price >= 100000:
        return int(price * 0.95)
    else:
        return price

print(solution(150000)) # 142500
print(solution(580000)) # 464000