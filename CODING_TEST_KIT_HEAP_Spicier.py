def mix_scoville(scoville, K):
    cnt = 0
    while min(scoville) < K:
        if len(scoville) == 1:
            cnt = -1
            break
        scoville.sort()
        min_degree = scoville.pop(0)
        second_degree = scoville.pop(0)
        mix_degree = min_degree+(second_degree*2)
        scoville.append(mix_degree)
        cnt += 1
    return cnt

def solution(scoville, K):
    answer = mix_scoville(scoville, K)
    return answer