def solution(my_string, n):
    answer = list(my_string)
    # answer = ['h', 'e', 'l', 'l', 'o']
    result = []

    for i in answer:
        result.append(i * n)
    
    return ''.join(result) 

print(solution("hello", 3)) # "hhheeellllllooo"
