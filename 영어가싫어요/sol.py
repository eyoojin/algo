def solution(numbers):
    answer = 0
    words = [ "zero", "one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]
    
    for i in range(len(words)):
        numbers = numbers.replace(words[i], str(i))
    return int(numbers)

print(solution('onetwothreefourfivesixseveneightnine')) # 1234567890
print(solution('onefourzerosixseven')) # 14067