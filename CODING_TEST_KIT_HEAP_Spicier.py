import heapq as hq

def mix_scoville(scoville, K):
    cnt = 0
    while scoville[0] < K:
        if len(scoville) == 1:
            cnt = -1
            break
        min_degree = hq.heappop(scoville)
        second_degree = hq.heappop(scoville)
        mix_degree = min_degree+(second_degree*2)
        hq.heappush(scoville, mix_degree)
        cnt += 1
    return cnt

def solution(scoville, K):
    hq.heapify(scoville)
    answer = mix_scoville(scoville, K)
    return answer

# error point: when use 'min' and 'sort'