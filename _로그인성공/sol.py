def solution(id_pw, db):
    answer = []

    for i in range(len(db)):
        if id_pw in db:
            return 'login'
        else:
            return 'fail'

# wrong pw...

print(solution(["meosseugi", "1234"], [["rardss", "123"], ["yyoom", "1234"], ["meosseugi", "1234"]])) # login
print(solution(["programmer01", "15789"], [["programmer02", "111111"], ["programmer00", "134"], ["programmer01", "1145"]])) # wrong pw
print(solution(["rabbit04", "98761"], [["jaja11", "98761"], ["krong0313", "29440"], ["rabbit00", "111333"]])) # fail
