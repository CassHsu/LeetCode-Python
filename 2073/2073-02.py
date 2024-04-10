class Solution:
    def timeRequiredToBuy(self, tickets: List[int], k: int) -> int:
        size = len(tickets)
        seconds = 0
        q = [0 for _ in range(size)]

        while q[k] < tickets[k]:
            for i in range(size):
                if q[k] == tickets[k] and i > k:
                    break

                if q[i] < tickets[i]:
                    q[i] += 1
                    seconds += 1

        return seconds
