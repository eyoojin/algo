def solution(my_string):
    answer = ''
    vowels = 'aeiou'
    for word in my_string:
        if word not in vowels:
            answer += word

    return answer

print(solution("bus")) # "bs"
print(solution("nice to meet you")) # "nc t mt y"