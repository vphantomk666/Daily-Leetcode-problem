class Solution:
    def countServers(self, m: int, logs: List[List[int]], x: int, queries: List[int]) -> List[int]:

        logs.sort(key = lambda log : log[1])
        n = len(logs)
        sort_que = sorted((q, i) for i, q in enumerate(queries))

        freq = {}
        res = [0]*len(queries)
        l = 0
        r = 0
        active = 0

        for q, idx in sort_que:

            while r < n and logs[r][1] <= q:
                server_id = logs[r][0]

                freq[server_id] = freq.get(server_id, 0) + 1

                if freq[server_id] == 1:
                    active += 1

                r += 1
            
            while l < n and logs[l][1] < q-x:
                server_id = logs[l][0]

                freq[server_id] -= 1

                if freq[server_id] == 0:
                    active -= 1
                    del freq[server_id]

                l += 1
            
            res[idx] = m-active
        

        return res
            





































        # brute-force approach
        # res = []

        # i = 0
        # while i < len(queries):
        #     active_servers = set()
        #     for server_id, time in logs:
        #         if queries[i] - x <= time <= queries[i]:
        #             active_servers.add(server_id)

        #     res.append(n - len(active_servers))

        #     i+=1
        

        # return res










        