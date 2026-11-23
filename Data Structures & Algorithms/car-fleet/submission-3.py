class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        time_ahead = -1
        res = 0
        for pos, speed in sorted(zip(position, speed), reverse=True):
            time = (target - pos) / speed
            if time > time_ahead:
                time_ahead = time
                res+=1
        return res