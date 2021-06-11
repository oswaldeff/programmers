def mix_scoville(scoville, K):
    cnt = 0
    while min(scoville) < K:
        if len(scoville) == 1:
            cnt = -1
            break
        min_degree = min(scoville)
        scoville.remove(min_degree)
        second_degree = min(scoville)
        scoville.remove(second_degree)
        mix_degree = min_degree+(second_degree*2)
        scoville.append(mix_degree)
        cnt += 1
    return cnt

def solution(scoville, K):
    scoville.sort()
    answer = mix_scoville(scoville, K)
    return answer