def solution(letter):
    morse = { 
    '.-':'a','-...':'b','-.-.':'c','-..':'d','.':'e','..-.':'f',
    '--.':'g','....':'h','..':'i','.---':'j','-.-':'k','.-..':'l',
    '--':'m','-.':'n','---':'o','.--.':'p','--.-':'q','.-.':'r',
    '...':'s','-':'t','..-':'u','...-':'v','.--':'w','-..-':'x',
    '-.--':'y','--..':'z'
    }
    answer = []
    for i in letter.split():
        for k, v in morse.items():
        
            if k == i:
                answer.append(v)
    return ''.join(answer)


print(solution(".... . .-.. .-.. ---")) # hello
print(solution(".--. -.-- - .... --- -.")) # python