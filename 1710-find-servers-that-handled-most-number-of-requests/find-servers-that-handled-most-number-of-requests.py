import heapq
from sortedcontainers import SortedList

class Solution:
    def busiestServers(self, k: int, arrival: list[int], load: list[int]) -> list[int]:
        n = len(arrival)

        available_server = SortedList(range(k))
        busy_server = []

        count_request = [0] * k

        for i in range(n):
            time = arrival[i]

            while busy_server and busy_server[0][0] <= time:
                free_time, server = heapq.heappop(busy_server)
                available_server.add(server)

            if not available_server:
                continue

            target = i % k

            idx = available_server.bisect_left(target)

            if idx == len(available_server):
                idx = 0

            target_server = available_server[idx]
            available_server.remove(target_server)

            heapq.heappush(
                busy_server,
                (time + load[i], target_server)
            )

            count_request[target_server] += 1

        max_requests = max(count_request)

        return [
            i for i in range(k)
            if count_request[i] == max_requests
        ]