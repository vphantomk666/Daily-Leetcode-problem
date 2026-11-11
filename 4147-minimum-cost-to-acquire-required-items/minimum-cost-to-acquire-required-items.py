class Solution:
    def minimumCost(self, cost1: int, cost2: int, costBoth: int, need1: int, need2: int) -> int:
        min_need = min(need1, need2)
        max_need = max(need1, need2)

        return min((costBoth*min_need + (need1-min_need)*cost1 + (need2-min_need)*cost2), (max_need*costBoth), (need1 * cost1 + need2 * cost2))
        