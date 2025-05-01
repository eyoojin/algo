def solution(my_str, n):
    answer = []
    for i in range(len(my_str)//n):
        answer.append(my_str[i*n:(i+1)*n])

    return answer, len(my_str)

print(solution('abc1Addfggg4556b', 6)) # ["abc1Ad", "dfggg4", "556b"]
print(solution('abcdef123', 3)) # ["abc", "def", "123"]