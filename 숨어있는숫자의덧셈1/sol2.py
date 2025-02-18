def solution(my_string):
    numbers = []

    for char in my_string:
        if char.isdigit(): # 숫자로 변형할 수 있는 것들을 내보내주는 메소드
            numbers.append(int(char))

    return sum(numbers)        

print(solution("aAb1B2cC34oOp")) # 10
print(solution("1a2b3c4d123")) # 16