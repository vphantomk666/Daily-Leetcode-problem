class Solution:
    def countDaysTogether(self, arriveAlice: str, leaveAlice: str,
        arriveBob: str, leaveBob: str) -> int:

        def to_days(date):
            month, day = map(int, date.split("-"))

            days_in_month = [31, 28, 31, 30, 31, 30,
                             31, 31, 30, 31, 30, 31]

            total = sum(days_in_month[:month - 1]) + day
            return total

        start = max(to_days(arriveAlice), to_days(arriveBob))
        end = min(to_days(leaveAlice), to_days(leaveBob))

        return max(0, end - start + 1)
