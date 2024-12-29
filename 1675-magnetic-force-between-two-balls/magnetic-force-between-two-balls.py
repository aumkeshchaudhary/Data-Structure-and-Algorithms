class Solution(object):
    def maxDistance(self, position, m):
        def can_place_balls(force):
            count = 1 
            last_position = position[0]
            for i in range(1, len(position)):
                if position[i] - last_position >= force:
                    count += 1
                    last_position = position[i]
                    if count == m:
                        return True
            return False
       
        position.sort()
        left, right = 1, position[-1] - position[0] 
        best_force = 0

        while left <= right:
            mid = (left + right) // 2
            if can_place_balls(mid):
                best_force = mid  
                left = mid + 1   
            else:
                right = mid - 1 

        return best_force