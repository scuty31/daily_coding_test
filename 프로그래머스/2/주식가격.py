import heapq


def solution(prices):
    answer = [0 for _ in range(len(prices))]
    queue = []

    for i in range(len(prices)):
        price = prices[i]
        if len(queue) == 0:
            heapq.heappush(queue, (-price, i))
            continue

        last_price, idx = queue[0]

        if -last_price > price:
            while queue and -queue[0][0] > price:
                prev_price, idx = heapq.heappop(queue)
                answer[idx] = i - idx

        heapq.heappush(queue, (-price, i))

    for price, idx in queue:
        answer[idx] = len(prices)-1 - idx

    return answer


input_prices = [1, 2, 3, 2, 3]
print(solution(input_prices))