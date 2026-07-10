class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        maximums = []
        candidates = deque()
        left = 0

        for right in range(len(nums)):
            # Remove candidates smaller than the new value. 
            while candidates and nums [candidates[-1]] < nums[right]:
                candidates.pop()

            candidates.append(right)

            # Remove the front candidate if it is outside the window.
            if candidates[0] < left:
                candidates.popleft()

            # Record the maximum once the window reaches size k.
            if right - left + 1 == k:
                maximums.append(nums[candidates[0]])
                left += 1

        return maximums