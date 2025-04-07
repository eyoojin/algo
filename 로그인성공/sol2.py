def solution(id_pw, db):
    answer = []

    if id_pw in db:
        return 'login'
    else:
        for i in db:
            if i[0] == id_pw[0]:
                answer.append(i)
        if len(answer) == 0:
            return 'fail'
        else:
            return 'wrong pw'


print(solution(["meosseugi", "1234"], [["rardss", "123"], ["yyoom", "1234"], ["meosseugi", "1234"]])) # login
print(solution(["programmer01", "15789"], [["programmer02", "111111"], ["programmer00", "134"], ["programmer01", "1145"]])) # wrong pw
print(solution(["rabbit04", "98761"], [["jaja11", "98761"], ["krong0313", "29440"], ["rabbit00", "111333"]])) # fail
