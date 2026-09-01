class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:

        pairs = list(zip(position, speed))
        pairs.sort(reverse=True)

        fleets = 0
        dis = 0

        for p, s in pairs:
            time = (target - p) / s

            if time > dis:
                fleets += 1
                dis = time

        return fleets