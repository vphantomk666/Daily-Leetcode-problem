class Solution:

    def find(self, x: int, parent: List[int]) -> int:
        if x != parent[x]:
            parent[x] = self.find(parent[x], parent)

        return parent[x]

    def Union(self, x: int, y: int, parent: List[int]) -> None:
        x_parent = self.find(x, parent)
        y_parent = self.find(y, parent)

        if x_parent != y_parent:
            parent[x_parent] = y_parent

    def lexicographicallySmallestArray(self, nums: List[int], limit: int) -> List[int]:

        n = len(nums)
        parent = list(range(n))
        result = [0] * n

        pairs = sorted(enumerate(nums), key=lambda x: x[1])

        for i in range(1, n):

            prev_index, prev_value = pairs[i - 1]
            curr_index, curr_value = pairs[i]

            if curr_value - prev_value <= limit:
                self.Union(prev_index, curr_index, parent)

        group = {}

        for i in range(n):
            root = self.find(i, parent)

            if root not in group:
                group[root] = []

            group[root].append(i)

        for indices in group.values():

            values = sorted(nums[i] for i in indices)

            indices.sort()

            for index, value in zip(indices, values):
                result[index] = value

        return result


        # i = 0

        # while i < n:
        #     j = i + 1

        #     while j < n and pairs[j][1] - pairs[j - 1][1] <= limit:
        #         j += 1

        #     keys = sorted(pairs[k][0] for k in range(i, j))
        #     values = [pairs[k][1] for k in range(i, j)]

        #     for key, value in zip(keys, values):
        #         result[key] = value

        #     i = j

        # return result