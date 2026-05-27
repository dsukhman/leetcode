class Solution(object):
    def trap(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        left = 0
        right = len(height) - 1

        water = [0]
        waterAmount = 0

        while left < right:
            block = min(height[left], height[right])
            if water[-1] > block:
                waterAmount = waterAmount + block - water[-1]
            else:
                water.append(block)

            if height[left] <= height[right]:
                left += 1
            else:
                right -= 1

        return waterAmount*-1
