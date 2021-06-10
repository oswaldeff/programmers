def mix_scoville(scoville, K):
    cnt = 0
    while min(scoville) < K:
        scoville.sort()
        min_degree = scoville[0]
        second_degree = scoville[1]
        mix_degree = min_degree+(second_degree*2)
        scoville.append(mix_degree)
        cnt += 1
    return cnt

def solution(scoville, K):
    answer = mix_scoville(scoville, K)
    return answer