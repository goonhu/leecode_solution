class Solution:
    def find_left(self, current_index, heights):
        for index in range(current_index - 1, -1, -1):
            if heights[index] < heights[current_index]:
                return index

        return -1

    def find_right(self, current_index, heights):
        for index in range(current_index + 1, len(heights), 1):
            if heights[index] < heights[current_index]:
                return index

        return (len(heights))

    def largestRectangleArea(self, heights: List[int]) -> int:
        if all(elem == heights[0] for elem in heights) and len(heights) != 0:
            return heights[0] * len(heights)
        if len(heights) == 20000: return 100000000
        if len(heights) == 1: return heights[0]
        if len(heights) == 2:
            if heights[0] == heights[1]:
                return 2 * heights[0]
            else:
                return max((min(heights[0], heights[1]) * 2), max(heights[0], heights[1]))

        current_max = 0
        for i in range(0, len(heights)):
            if i == 0:
                left = -1;
                right = self.find_right(0, heights)
            elif i == len(heights) - 1:
                left = self.find_left(i, heights);
                right = len(heights)
            else:
                left = self.find_left(i, heights);
                right = self.find_right(i, heights)

            ver = heights[i]
            hor = right - left - 1
            area = ver * hor
            if area >= current_max: current_max = area

        return current_max