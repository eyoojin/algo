def solution(my_string):
    answer = 0
    word1 = 'qwertyuiopasdfghjklzxcvbnm'
    word2 = 'QWERTYUIOPASDFGHJKLZXCVBNM'

    for i in word1:
        my_string = my_string.replace(i, 'a')

    for j in word2:
        my_string = my_string.replace(j, 'a')

    my_string = my_string.split(sep='a')

    for k in range(len(my_string)):
        if my_string[k] == '':
            my_string.pop(k)


    return my_string

print(solution('aAb1B2cC34oOp')) # 37
print(solution('1a2b3c4d123Z')) # 133
