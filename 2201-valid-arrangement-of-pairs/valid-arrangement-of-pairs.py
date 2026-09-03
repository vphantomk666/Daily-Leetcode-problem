from collections import defaultdict
class Solution:
    def validArrangement(self, pairs: List[List[int]]) -> List[List[int]]:
        adj = defaultdict(list)

        indegree = defaultdict(int)
        outdegree = defaultdict(int)

        for u, v in pairs:
            adj[u].append(v)
            outdegree[u] += 1
            indegree[v] += 1


        StartNode = pairs[0][0]

        for node in adj:
            if outdegree[node] - indegree[node] == 1:
                StartNode = node
                break
            
        EulerPath = []

        st = []

        st.append(StartNode)

        while st:
            curr = st[-1]
            if adj[curr]:
                ngbr = adj[curr].pop()
                st.append(ngbr)
            
            else:
                EulerPath.append(curr)
                st.pop()

        newEp = EulerPath[::-1]

        result = []

        for i in range(len(EulerPath)-1):
            result.append([newEp[i],newEp[i+1]])
        
        return result

