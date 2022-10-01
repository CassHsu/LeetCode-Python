class Solution:
    def getSkyline(self, buildings: List[List[int]]) -> List[List[int]]:
        n = len(buildings)
        
        if n == 0: return []
        if n == 1: return [[buildings[0][0], buildings[0][2]], [buildings[0][1], 0]]
        
        left_skyline = self.getSkyline(buildings[: n // 2])
        right_skyline = self.getSkyline(buildings[n // 2 :])  
        
        return self.merge_sky(left_skyline, right_skyline)
    
    def merge_sky(self, left_skyline, right_skyline):
        answer = []
        left_pos, right_pos = 0, 0
        left_prev_height, right_prev_height = 0, 0
        
        while left_pos < len(left_skyline) and right_pos < len(right_skyline):
            next_left_x = left_skyline[left_pos][0]
            next_right_x = right_skyline[right_pos][0]

            if next_left_x < next_right_x:
                left_prev_height = left_skyline[left_pos][1]
                cur_x = next_left_x
                cur_y = max(left_prev_height, right_prev_height)
                left_pos += 1
                
            elif next_left_x > next_right_x:
                right_prev_height = right_skyline[right_pos][1]
                cur_x = next_right_x
                cur_y = max(left_prev_height, right_prev_height)
                right_pos += 1

            else:
                left_prev_height = left_skyline[left_pos][1]
                right_prev_height = right_skyline[right_pos][1]
                cur_x = next_left_x
                cur_y = max(left_prev_height, right_prev_height)
                left_pos += 1
                right_pos += 1
                
            if not answer or answer[-1][1] != cur_y:
                answer.append([cur_x, cur_y])
                
        while left_pos < len(left_skyline):
            answer.append(left_skyline[left_pos])
            left_pos += 1
            
        while right_pos < len(right_skyline):
            answer.append(right_skyline[right_pos])
            right_pos += 1

        return answer
