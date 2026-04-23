class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        pair = [(p,s) for p , s in zip(position, speed)]
        pair.sort(reverse=True)
        prev_time = ((target - pair[0][0])/pair[0][1])
        fleet = 1
        for car in pair:
            curr_time = ((target - car[0]) / car[1])
            if curr_time <= prev_time:
                continue
            else:
                fleet += 1
            prev_time = max(prev_time, curr_time)    
        return fleet