
class Solution:
    def maxArea(self, height):
        head = 0;
        tail = len(height) - 1
        current_water = 0
        while (head < tail):
            if height[head] > height[tail]:
                water = abs(head - tail) * height[tail]
                tail -= 1
            else:
                water = abs(head - tail) * height[head]
                head += 1
            if water > current_water: current_water = water

        return current_water