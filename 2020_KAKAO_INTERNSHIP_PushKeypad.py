def solution(numbers, hand):
    keypad = {
        '*': (0, 7),
        '#': (0, 9),
        0: ('*', '#', 8),
        1: (2, 4),
        2: (1, 3, 5),
        3: (2, 6),
        4: (1, 5, 7),
        5: (2, 4, 6, 8),
        6: (3, 5, 9),
        7: ('*', 4, 8),
        8: (0, 5, 7, 9),
        9: ('#', 6, 8)
    }

    x_y_location = {
        '*': (0, 0),
        0: (1, 0),
        '#': (2, 0),
        7: (0, 1),
        8: (1, 1),
        9: (2, 1),
        4: (0, 2),
        5: (1, 2),
        6: (2, 2),
        1: (0, 3),
        2: (1, 3),
        3: (2, 3)
    }
    
    answer = ""
    
    left = (1, 4, 7, '*')
    right = (3, 6, 9, '#')
    mid = (0, 2, 5, 8)
    
    location = {
        'left': '*',
        'right': '#'
    }
    
    for n in numbers:
        if n in left:
            location['left'] = n
            answer += "L"
            continue
        if n in right:
            location['right'] = n
            answer += "R"
            continue
        if n in mid:
            if (location['left'] in keypad[n]) and (location['right'] not in keypad[n]):
                location['left'] = n
                answer += "L"
                continue
            if (location['right'] in keypad[n]) and (location['left'] not in keypad[n]):
                location['right'] = n
                answer += "R"
                continue
            if (location['left'] in keypad[n]) and (location['right'] in keypad[n]):
                location[hand] = n
                if hand == 'left':
                    answer += "L"
                    continue
                if hand == 'right':
                    answer += "R"
                    continue
            if (location['left'] not in keypad[n]) and (location['right'] not in keypad[n]):
                left_dist = int()
                right_dist = int()
                left_dist = abs(x_y_location[n][0] - x_y_location[location['left']][0]) + abs(x_y_location[n][1] - x_y_location[location['left']][1])
                right_dist = abs(x_y_location[n][0] - x_y_location[location['right']][0]) + abs(x_y_location[n][1] - x_y_location[location['right']][1])
                
                if left_dist < right_dist:
                    answer += "L"
                    continue
                if left_dist > right_dist:
                    answer += "R"
                    continue
                if left_dist == right_dist:
                    if hand == 'left':
                        answer += "L"
                        continue
                    if hand == 'right':
                        answer += "R"                    
    print(answer)
    return answer

solution([1, 3, 4, 5, 8, 2, 1, 4, 5, 9, 5], "right") # "LRLLLRLLRRL"
solution([7, 0, 8, 2, 8, 3, 1, 5, 7, 6, 2], "left") # "LRLLRRLLLRR"
solution([1, 2, 3, 4, 5, 6, 7, 8, 9, 0], "right") # "LLRLLRLLRL"