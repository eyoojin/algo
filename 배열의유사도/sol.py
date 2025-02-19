def solution(s1, s2):
    s1_set = set(s1)
    s2_set = set(s2)
    
    answer = len(s1_set & s2_set)
    
    return answer

print(solution(["a", "b", "c"], ["com", "b", "d", "p", "c"])) # 2
print(solution(["n", "omg"], ["m", "dot"])) # 0