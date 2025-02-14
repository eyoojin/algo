def solution(n, k):
    # n : 양꼬치 인분 수 / k : 음료수 개수
    answer = 0

    # 양꼬치 총액 + 음료수 총액 - 서비스 음료수 가격
    answer = (n * 12000) + (k * 2000) - (n//10 * 2000)
    
    return answer
    
print(solution(10, 3)) # 124000
print(solution(64, 6)) # 768000