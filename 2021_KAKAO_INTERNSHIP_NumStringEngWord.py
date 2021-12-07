eng_to_num = {
    'zero': '0',
    'one': '1',
    'two': '2',
    'three': '3',
    'four': '4',
    'five': '5',
    'six': '6',
    'seven': '7',
    'eight': '8',
    'nine': '9'
}

def solution(s):
    keys = list(eng_to_num.keys())
    for key in keys:
        if key in s:
            s = s.replace(key, eng_to_num[key])
            
    s = int(s)
    answer = s
    print(answer)
    return answer

solution("one4seveneight") # 1478
solution("23four5six7") # 234567
solution("2three45sixseven") # 234567