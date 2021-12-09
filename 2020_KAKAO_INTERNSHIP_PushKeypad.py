keypad = {
        '*': [0, 7],
        '#': [0, 9],
        0: ['*', '#', 8],
        1: [2, 4],
        2: [1, 3, 5],
        3: [2, 6],
        4: [1, 5, 7],
        5: [2, 4, 6, 8],
        6: [3, 5, 9],
        7: ['*', 4, 8],
        8: [0, 5, 7, 9],
        9: ['#', 6, 8]
    }

def solution(numbers, hand):
    answer = ""
    
    left = [1, 4, 7, '*']
    right = [3, 6, 9, '#']
    mid = [0, 2, 5, 8]
    
    location = {
        'left': '*',
        'right': '#'
    }
    
    for n in numbers:
        if n in left:
            location['left'] = n
            answer += "L"
        if n in right:
            location['right'] = n
            answer += "R"
        if n in mid:
            if location['left'] in keypad[n] and location['right'] not in keypad[n]:
                location['left'] = n
                answer += "L"
                continue
            if location['right'] in keypad[n] and location['left'] not in keypad[n]:
                location['right'] = n
                answer += "R"
                continue
            if location['left'] and location['right'] in keypad[n]:
                location[hand] = n
                if hand == 'left':
                    answer += "L"
                if hand == 'right':
                    answer += "R"
                continue
            if location['left'] and location['right'] not in keypad[n]:
                D = False
                for i in keypad[location['left']]:
                    if i in keypad[n]:
                        location['left'] = n
                        answer += "L"
                        D = True
                        break
                if D == False:
                    for j in keypad[location['right']]:
                        if j in keypad[n]:
                            location['right'] = n
                            answer += "R"
                            break
    print(answer)
    return answer

solution([1, 3, 4, 5, 8, 2, 1, 4, 5, 9, 5], "right") # "LRLLLRLLRRL"
solution([7, 0, 8, 2, 8, 3, 1, 5, 7, 6, 2], "left") # "LRLLRRLLLRR"
solution([1, 2, 3, 4, 5, 6, 7, 8, 9, 0], "right") # "LLRLLRLLRL"