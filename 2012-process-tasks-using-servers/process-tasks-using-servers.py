import heapq

class Solution:
    def assignTasks(self, servers: list[int], tasks: list[int]) -> list[int]:

        free_Server = []
        busy_Server = []

        result = [0] * len(tasks)

        for i, server in enumerate(servers):
            heapq.heappush(free_Server, [server, i])

        time = 0

        for i, task in enumerate(tasks):

            time = max(time, i)

            while busy_Server and busy_Server[0][0] <= time:
                finish, weight, idx = heapq.heappop(busy_Server)
                heapq.heappush(free_Server, [weight, idx])

            if not free_Server:
                time = busy_Server[0][0]

                while busy_Server and busy_Server[0][0] <= time:
                    finish, weight, idx = heapq.heappop(busy_Server)
                    heapq.heappush(free_Server, [weight, idx])

            weight, idx = heapq.heappop(free_Server)

            result[i] = idx

            heapq.heappush(
                busy_Server,
                [time + task, weight, idx]
            )

        return result