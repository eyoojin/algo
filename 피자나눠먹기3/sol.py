def solution(slice, n):
        
    if n % slice == 0:
        return n // slice
    else:
        return n // slice + 1

print(solution(7, 10)) # 2
print(solution(4, 12)) # 3