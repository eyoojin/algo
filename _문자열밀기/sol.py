def solution(A, B):
    answer = []

    if A == B:
        return 0

    A = list(A)

    for i in range(len(A)):
        a = A.pop()
        A = [a] + A
        print(A)

    if list(B) in answer:
        return answer
    else:
        return -1

print(solution('asdf', 'dfas'))
print(solution('hello', 'ohell')) # 1
print(solution('apple', 'elppa')) # -1
print(solution('atat', 'tata')) # 1
print(solution('abc', 'abc')) # 0
