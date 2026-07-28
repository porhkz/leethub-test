class Solution:
    def maxArea(self, height: List[int]) -> int:
        right = len(height) - 1
        left = 1

        x = height[right] - 0
        y = min(height[0], height[right]) 

        max_vol = x * y

        for left in range(len(height)):
            x = right - left
            y = min(height[left], height[right]) 

            max_vol = max(max_vol, x * y)

            right = right - 1

            x = right - left
            y = min(height[left], height[right]) 

            max_vol = max(max_vol, x * y)

        return max_vol





            