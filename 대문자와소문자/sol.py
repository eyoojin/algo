def solution(my_string):
    answer = list(my_string)
    result = []
    big = list('ABCDEFGHIJKLMNOPQRSTUVWXYZ')
    small = list('abcdefghijklmnopqrstuvwxyz')

    for i in range(len(answer)):
        if answer[i] in big:
            for a in range(len(big)):
                if answer[i] == big[a]:
                    answer[i] = small[a]
                    result.append(answer[i])
        else:            
            for b in range(len(small)):
                if answer[i] == small[b]:
                    answer[i] = big[b]
                    result.append(answer[i])

    return ''.join(result)


print(solution("cccCCC")) # "CCCccc"
print(solution("abCdEfghIJ")) # "ABcDeFGHij"