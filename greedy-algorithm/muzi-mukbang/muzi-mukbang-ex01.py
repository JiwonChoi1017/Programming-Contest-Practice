import heapq


# ムジのモクバン
def solution(food_times, k):
    # 全部食べ切った場合-1をリターン
    if sum(food_times) <= k:
        return -1

    q = []
    length = len(food_times)
    # 最小値から取り出すため、優先度付きキューを使用
    for i in range(length):
        heapq.heappush(q, (food_times[i], i + 1))

    sum_value = 0
    pre = 0

    while sum_value + ((q[0][0] - pre) * length) <= k:
        now = heapq.heappop(q)[0]
        sum_value += (now - pre) * length
        length -= 1
        pre = now

    answer = sorted(q, key=lambda x: x[1])
    return answer[(k - sum_value) % length][1]
