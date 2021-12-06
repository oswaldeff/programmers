ranking = {
    6: 1,
    5: 2,
    4: 3,
    3: 4,
    2: 5,
    1: 6,
    0: 6
}

def solution(lottos, win_nums):
    zero_cnt = 0
    coincide_cnt = 0
    for num in lottos:
        if num == 0:
            zero_cnt += 1
        if num != 0:
            if num in win_nums:
                coincide_cnt += 1
    
    answer = [ranking[zero_cnt+coincide_cnt], ranking[coincide_cnt]]
    print(answer)
    return answer

solution([44, 1, 0, 0, 31, 25], [31, 10, 45, 1, 6, 19]) # [3, 5]
solution([0, 0, 0, 0, 0, 0], [38, 19, 20, 40, 15, 25]) # [1, 6]
solution([45, 4, 35, 20, 3, 9], [20, 9, 3, 45, 4, 35]) # [1, 1]